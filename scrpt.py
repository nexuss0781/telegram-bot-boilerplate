import sys, os
sys.path.insert(0, "api")

from database import init_db, SessionLocal
from auth import (
    create_user,
    authenticate_user,
    create_session_token,
    get_user_by_token,
    delete_session,
    link_telegram,
    unlink_telegram,
    get_user_by_chat_id,
    hash_password,
    verify_password,
)
from models import User, Session

PASS = "✅ PASS"
FAIL = "❌ FAIL"

os.environ["TOKEN"] = "test"

init_db()

results = []
def check(name, ok):
    print(f"{PASS if ok else FAIL} {name}")
    results.append((name, ok))

db = SessionLocal()


# ── password hashing ──────────────────────────
hashed = hash_password("secret123")
check("hash_password returns salt:hash format", ":" in hashed)
check("verify_password correct", verify_password("secret123", hashed))
check("verify_password wrong", not verify_password("wrong", hashed))

# ── create_user ───────────────────────────────
u1 = create_user("Alice", "alice@test.com", "+111", "pass1")
check("create_user returns user object", u1 is not None)
check("create_user sets full_name", u1.full_name == "Alice")
check("create_user sets email", u1.email == "alice@test.com")
check("create_user sets phone", u1.phone == "+111")
check("create_user hashed password stored", u1.password_hash != "pass1")

u1_dup = create_user("Alice Dup", "alice@test.com", "+222", "pass2")
check("create_user duplicate email returns None", u1_dup is None)

# ── authenticate_user ─────────────────────────
au_ok = authenticate_user("alice@test.com", "pass1")
check("authenticate_user correct creds", au_ok is not None and au_ok.email == "alice@test.com")

au_bad_pw = authenticate_user("alice@test.com", "wrong")
check("authenticate_user wrong password", au_bad_pw is None)

au_bad_email = authenticate_user("nobody@test.com", "pass1")
check("authenticate_user unknown email", au_bad_email is None)

# ── session tokens ────────────────────────────
token = create_session_token(u1.id)
check("create_session_token returns string", isinstance(token, str) and len(token) > 20)

u_by_token = get_user_by_token(token)
check("get_user_by_token finds user", u_by_token is not None and u_by_token.id == u1.id)

check("get_user_by_token returns correct user", u_by_token.email == "alice@test.com")

u_bad_token = get_user_by_token("invalid_token_xyz")
check("get_user_by_token invalid token", u_bad_token is None)

delete_session(token)
u_deleted = get_user_by_token(token)
check("delete_session removes session", u_deleted is None)

# ── telegram linking ──────────────────────────
u2 = create_user("Bob", "bob@test.com", "+333", "pass3")
link_telegram(u2, "12345")

u_by_chat = get_user_by_chat_id("12345")
check("get_user_by_chat_id finds user", u_by_chat is not None and u_by_chat.email == "bob@test.com")
check("link_telegram sets chat_id", u_by_chat is not None and u_by_chat.telegram_chat_id == "12345")

u_by_chat_none = get_user_by_chat_id("99999")
check("get_user_by_chat_id unknown chat", u_by_chat_none is None)

unlinked = unlink_telegram("12345")
check("unlink_telegram returns user dict", unlinked is not None and unlinked["email"] == "bob@test.com")

after_unlink = get_user_by_chat_id("12345")
check("unlink_telegram clears chat_id", after_unlink is None)

unlinked_none = unlink_telegram("99999")
check("unlink_telegram unknown chat returns None", unlinked_none is None)


# ── summary ───────────────────────────────────
print(f"\n{'='*40}")
passed = sum(1 for _, ok in results if ok)
total = len(results)
print(f"Results: {passed}/{total} passed")
if passed == total:
    print(f"{PASS} All checks passed!")
else:
    print(f"{FAIL} {total - passed} failure(s)")

db.close()
