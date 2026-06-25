BASE_CSS = """
:root {
  --deep-blue: #1B325F;
  --teal: #5E9FA3;
  --beige: #DCD1B4;
  --orange: #FAB87F;
  --coral: #F87E7B;
  --rose: #B05574;
  --bg: #0a0f1e;
  --bg-card: rgba(255,255,255,0.04);
  --border: rgba(255,255,255,0.08);
  --text: #e2e8f0;
  --text-muted: #94a3b8;
  --nav-bg: rgba(10,15,30,0.7);
}
.light {
  --bg: #f5f0e8;
  --bg-card: rgba(255,255,255,0.6);
  --border: rgba(0,0,0,0.08);
  --text: #1e293b;
  --text-muted: #64748b;
  --nav-bg: rgba(245,240,232,0.8);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  transition: background 0.3s, color 0.3s;
  line-height: 1.6;
}
.glass {
  background: var(--bg-card);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 16px;
}
.nav-glass {
  background: var(--nav-bg);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
.glow {
  box-shadow: 0 0 40px rgba(94,159,163,0.08);
}
.btn-primary {
  background: linear-gradient(135deg, var(--teal), var(--deep-blue));
  color: #fff;
  padding: 12px 28px;
  border-radius: 12px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 0.95rem;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(94,159,163,0.3);
}
.btn-secondary {
  background: var(--bg-card);
  color: var(--text);
  padding: 12px 28px;
  border-radius: 12px;
  border: 1px solid var(--border);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 0.95rem;
}
.btn-secondary:hover {
  background: rgba(255,255,255,0.08);
}
.input-field {
  width: 100%;
  padding: 14px 16px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  color: var(--text);
  font-size: 0.95rem;
  outline: none;
  transition: border 0.3s;
}
.input-field:focus {
  border-color: var(--teal);
}
.input-field::placeholder {
  color: var(--text-muted);
}
.theme-toggle {
  cursor: pointer;
  padding: 8px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}
.animate-in {
  animation: fadeInUp 0.6s ease-out;
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.bg-gradient {
  background: linear-gradient(135deg, var(--deep-blue), #0a0f1e 50%, var(--deep-blue));
}
.light .bg-gradient {
  background: linear-gradient(135deg, #e8e0d0, #f5f0e8 50%, #e8e0d0);
}
.feature-card {
  transition: all 0.3s;
}
.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(94,159,163,0.12);
}
.accent-teal { color: var(--teal); }
.accent-orange { color: var(--orange); }
.accent-rose { color: var(--rose); }
"""


def landing_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Trusted</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}</style>
</head>
<body class="bg-gradient">
<nav class="nav-glass fixed top-0 left-0 right-0 z-50 px-6 py-4">
  <div class="max-w-6xl mx-auto flex items-center justify-between">
    <a href="/" class="flex items-center gap-2 text-xl font-bold" style="color:var(--teal)">
      <i data-lucide="shield-check" size="24"></i>
      <span>Trusted</span>
    </a>
    <div class="flex items-center gap-4">
      <a href="/login" class="text-sm font-medium hover:opacity-80 transition" style="color:var(--text-muted)">Log in</a>
      <a href="/signup" class="btn-primary text-sm !py-2 !px-5">Get started</a>
      <button class="theme-toggle" onclick="toggleTheme()">
        <i data-lucide="moon" size="18" id="theme-icon"></i>
      </button>
    </div>
  </div>
</nav>

<main class="pt-24">
  <section class="max-w-6xl mx-auto px-6 py-20 md:py-32">
    <div class="text-center max-w-3xl mx-auto animate-in">
      <div class="inline-flex items-center gap-2 glass !px-4 !py-2 mb-8 text-sm" style="color:var(--teal)">
        <i data-lucide="shield" size="14"></i>
        <span>Secure & Trusted Platform</span>
      </div>
      <h1 class="text-4xl md:text-6xl font-extrabold leading-tight mb-6" style="color:var(--text)">
        Your trusted space for
        <span style="color:var(--teal)">secure</span>
        <span style="color:var(--orange)">connections</span>
      </h1>
      <p class="text-lg md:text-xl mb-10" style="color:var(--text-muted); max-width:600px; margin-left:auto; margin-right:auto;">
        A simple, secure platform with Telegram integration.
        Sign up in seconds, connect with confidence.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="/signup" class="btn-primary text-lg !py-4 !px-10">Create your account</a>
        <a href="/login" class="btn-secondary text-lg !py-4 !px-10">
          <i data-lucide="log-in" size="18" class="inline mr-2"></i>Log in
        </a>
      </div>
    </div>
  </section>

  <section class="max-w-6xl mx-auto px-6 py-20">
    <div class="text-center mb-16 animate-in">
      <h2 class="text-3xl md:text-4xl font-bold mb-4">Built for trust</h2>
      <p style="color:var(--text-muted)" class="text-lg">Everything you need in one place</p>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="glass p-8 feature-card animate-in">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:rgba(94,159,163,0.15); color:var(--teal)">
          <i data-lucide="user-plus" size="24"></i>
        </div>
        <h3 class="text-xl font-semibold mb-3">Simple Sign Up</h3>
        <p style="color:var(--text-muted)">Create your account with just your name, email, and phone. No verification hassles.</p>
      </div>
      <div class="glass p-8 feature-card animate-in">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:rgba(250,184,127,0.15); color:var(--orange)">
          <i data-lucide="message-circle" size="24"></i>
        </div>
        <h3 class="text-xl font-semibold mb-3">Telegram Integration</h3>
        <p style="color:var(--text-muted)">Connect your account to Telegram for seamless notifications and bot commands.</p>
      </div>
      <div class="glass p-8 feature-card animate-in">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:rgba(176,85,116,0.15); color:var(--rose)">
          <i data-lucide="lock" size="24"></i>
        </div>
        <h3 class="text-xl font-semibold mb-3">Secure by Design</h3>
        <p style="color:var(--text-muted)">Your data is encrypted and protected. We take your privacy seriously.</p>
      </div>
    </div>
  </section>
</main>

<footer class="border-t" style="border-color:var(--border);">
  <div class="max-w-6xl mx-auto px-6 py-8 text-center text-sm" style="color:var(--text-muted)">
    <p>&copy; 2026 Trusted. All rights reserved.</p>
  </div>
</footer>

<script>
let dark = localStorage.getItem('theme') !== 'light';
document.documentElement.classList.toggle('light', !dark);
function toggleTheme() {{
  dark = !dark;
  document.documentElement.classList.toggle('light', !dark);
  localStorage.setItem('theme', dark ? 'dark' : 'light');
  document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
  lucide.createIcons();
}}
lucide.createIcons();
document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
lucide.createIcons();
</script>
</body>
</html>"""


def signup_page(error: str = ""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sign Up - Trusted</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}
.auth-container {{
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}
.auth-card {{
  width: 100%;
  max-width: 420px;
  padding: 40px;
}}
</style>
</head>
<body class="bg-gradient">
<nav class="nav-glass fixed top-0 left-0 right-0 z-50 px-6 py-4">
  <div class="max-w-6xl mx-auto flex items-center justify-between">
    <a href="/" class="flex items-center gap-2 text-xl font-bold" style="color:var(--teal)">
      <i data-lucide="shield-check" size="24"></i>
      <span>Trusted</span>
    </a>
    <div class="flex items-center gap-4">
      <a href="/login" class="text-sm font-medium hover:opacity-80 transition" style="color:var(--text-muted)">Log in</a>
      <button class="theme-toggle" onclick="toggleTheme()">
        <i data-lucide="moon" size="18" id="theme-icon"></i>
      </button>
    </div>
  </div>
</nav>

<div class="auth-container">
  <div class="glass auth-card animate-in">
    <div class="text-center mb-8">
      <div class="w-14 h-14 rounded-2xl flex items-center justify-center mx-auto mb-4" style="background:rgba(94,159,163,0.15); color:var(--teal)">
        <i data-lucide="user-plus" size="28"></i>
      </div>
      <h1 class="text-2xl font-bold">Create your account</h1>
      <p style="color:var(--text-muted)" class="text-sm mt-2">Join Trusted in seconds</p>
    </div>

    {"".join(f'<div class="mb-4 p-3 rounded-lg text-sm" style="background:rgba(248,126,123,0.1); color:var(--coral); border:1px solid rgba(248,126,123,0.2);">{error}</div>' for _ in [1] if error)}

    <form method="POST" action="/signup" class="space-y-4">
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Full name</label>
        <input type="text" name="full_name" required placeholder="John Doe" class="input-field">
      </div>
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Email</label>
        <input type="email" name="email" required placeholder="john@example.com" class="input-field">
      </div>
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Phone number</label>
        <input type="tel" name="phone" required placeholder="+1 234 567 890" class="input-field">
      </div>
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Password</label>
        <input type="password" name="password" required placeholder="Choose a strong password" class="input-field" minlength="6">
      </div>
      <button type="submit" class="btn-primary w-full !py-3.5">Create account</button>
    </form>

    <p class="text-center mt-6 text-sm" style="color:var(--text-muted)">
      Already have an account?
      <a href="/login" class="font-medium" style="color:var(--teal)">Log in</a>
    </p>
  </div>
</div>

<script>
let dark = localStorage.getItem('theme') !== 'light';
document.documentElement.classList.toggle('light', !dark);
lucide.createIcons();
document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
lucide.createIcons();
function toggleTheme() {{
  dark = !dark;
  document.documentElement.classList.toggle('light', !dark);
  localStorage.setItem('theme', dark ? 'dark' : 'light');
  document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
  lucide.createIcons();
}}
</script>
</body>
</html>"""


def login_page(error: str = ""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Log In - Trusted</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}
.auth-container {{
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}
.auth-card {{
  width: 100%;
  max-width: 420px;
  padding: 40px;
}}
</style>
</head>
<body class="bg-gradient">
<nav class="nav-glass fixed top-0 left-0 right-0 z-50 px-6 py-4">
  <div class="max-w-6xl mx-auto flex items-center justify-between">
    <a href="/" class="flex items-center gap-2 text-xl font-bold" style="color:var(--teal)">
      <i data-lucide="shield-check" size="24"></i>
      <span>Trusted</span>
    </a>
    <div class="flex items-center gap-4">
      <a href="/signup" class="text-sm font-medium hover:opacity-80 transition" style="color:var(--text-muted)">Sign up</a>
      <button class="theme-toggle" onclick="toggleTheme()">
        <i data-lucide="moon" size="18" id="theme-icon"></i>
      </button>
    </div>
  </div>
</nav>

<div class="auth-container">
  <div class="glass auth-card animate-in">
    <div class="text-center mb-8">
      <div class="w-14 h-14 rounded-2xl flex items-center justify-center mx-auto mb-4" style="background:rgba(94,159,163,0.15); color:var(--teal)">
        <i data-lucide="log-in" size="28"></i>
      </div>
      <h1 class="text-2xl font-bold">Welcome back</h1>
      <p style="color:var(--text-muted)" class="text-sm mt-2">Log in to your account</p>
    </div>

    {"".join(f'<div class="mb-4 p-3 rounded-lg text-sm" style="background:rgba(248,126,123,0.1); color:var(--coral); border:1px solid rgba(248,126,123,0.2);">{error}</div>' for _ in [1] if error)}

    <form method="POST" action="/login" class="space-y-4">
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Email</label>
        <input type="email" name="email" required placeholder="john@example.com" class="input-field">
      </div>
      <div>
        <label class="text-sm font-medium block mb-2" style="color:var(--text-muted)">Password</label>
        <input type="password" name="password" required placeholder="Enter your password" class="input-field">
      </div>
      <button type="submit" class="btn-primary w-full !py-3.5">Log in</button>
    </form>

    <p class="text-center mt-6 text-sm" style="color:var(--text-muted)">
      Don't have an account?
      <a href="/signup" class="font-medium" style="color:var(--teal)">Sign up</a>
    </p>
  </div>
</div>

<script>
let dark = localStorage.getItem('theme') !== 'light';
document.documentElement.classList.toggle('light', !dark);
lucide.createIcons();
document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
lucide.createIcons();
function toggleTheme() {{
  dark = !dark;
  document.documentElement.classList.toggle('light', !dark);
  localStorage.setItem('theme', dark ? 'dark' : 'light');
  document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
  lucide.createIcons();
}}
</script>
</body>
</html>"""


def dashboard_page(user, telegram_link_msg: str = ""):
    tg_status = "Connected" if user.telegram_chat_id else "Not connected"
    tg_icon = "check-circle" if user.telegram_chat_id else "message-circle"
    tg_color = "var(--teal)" if user.telegram_chat_id else "var(--text-muted)"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard - Trusted</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}
.dash-container {{
  max-width: 720px;
  margin: 0 auto;
  padding: 24px;
}}
</style>
</head>
<body class="bg-gradient">
<nav class="nav-glass fixed top-0 left-0 right-0 z-50 px-6 py-4">
  <div class="max-w-6xl mx-auto flex items-center justify-between">
    <a href="/" class="flex items-center gap-2 text-xl font-bold" style="color:var(--teal)">
      <i data-lucide="shield-check" size="24"></i>
      <span>Trusted</span>
    </a>
    <div class="flex items-center gap-4">
      <span class="text-sm" style="color:var(--text-muted)">{user.full_name}</span>
      <a href="/logout" class="btn-secondary text-sm !py-2 !px-4">
        <i data-lucide="log-out" size="16" class="inline mr-1"></i>Log out
      </a>
      <button class="theme-toggle" onclick="toggleTheme()">
        <i data-lucide="moon" size="18" id="theme-icon"></i>
      </button>
    </div>
  </div>
</nav>

<div class="dash-container" style="padding-top:100px">
  <div class="animate-in">
    <div class="flex items-center gap-4 mb-8">
      <div class="w-14 h-14 rounded-2xl flex items-center justify-center" style="background:rgba(94,159,163,0.15); color:var(--teal)">
        <i data-lucide="user" size="28"></i>
      </div>
      <div>
        <h1 class="text-2xl font-bold">Welcome, {user.full_name}</h1>
        <p style="color:var(--text-muted)" class="text-sm">Your account dashboard</p>
      </div>
    </div>

    {"".join(f'<div class="mb-4 p-3 rounded-lg text-sm" style="background:rgba(94,159,163,0.1); color:var(--teal); border:1px solid rgba(94,159,163,0.2);">{telegram_link_msg}</div>' for _ in [1] if telegram_link_msg)}

    <div class="glass p-8 mb-6">
      <h2 class="text-lg font-semibold mb-4">Account details</h2>
      <div class="space-y-3">
        <div class="flex items-center justify-between py-2" style="border-bottom:1px solid var(--border)">
          <span style="color:var(--text-muted)">Full name</span>
          <span class="font-medium">{user.full_name}</span>
        </div>
        <div class="flex items-center justify-between py-2" style="border-bottom:1px solid var(--border)">
          <span style="color:var(--text-muted)">Email</span>
          <span class="font-medium">{user.email}</span>
        </div>
        <div class="flex items-center justify-between py-2" style="border-bottom:1px solid var(--border)">
          <span style="color:var(--text-muted)">Phone</span>
          <span class="font-medium">{user.phone}</span>
        </div>
        <div class="flex items-center justify-between py-2">
          <span style="color:var(--text-muted)">Member since</span>
          <span class="font-medium">{user.created_at.strftime("%B %d, %Y") if user.created_at else "-"}</span>
        </div>
      </div>
    </div>

    <div class="glass p-8">
      <h2 class="text-lg font-semibold mb-4">Telegram connection</h2>
      <div class="flex items-center gap-3 mb-4">
        <i data-lucide="{tg_icon}" size="20" style="color:{tg_color}"></i>
        <span class="font-medium">{tg_status}</span>
      </div>
      <p style="color:var(--text-muted)" class="text-sm">
        Send <strong>/login</strong> to the bot to connect your Telegram account.
        Use <strong>/logoff</strong> to disconnect.
      </p>
    </div>
  </div>
</div>

<script>
let dark = localStorage.getItem('theme') !== 'light';
document.documentElement.classList.toggle('light', !dark);
lucide.createIcons();
document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
lucide.createIcons();
function toggleTheme() {{
  dark = !dark;
  document.documentElement.classList.toggle('light', !dark);
  localStorage.setItem('theme', dark ? 'dark' : 'light');
  document.getElementById('theme-icon').setAttribute('data-lucide', dark ? 'moon' : 'sun');
  lucide.createIcons();
}}
</script>
</body>
</html>"""
