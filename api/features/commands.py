from telegram import Update, Bot
from auth import get_user_by_chat_id, unlink_telegram
import os

BASE_URL = os.environ.get("BASE_URL", "https://trusted.vercel.app")


async def handle_update(update: Update, bot: Bot):
    text = update.message.text
    chat_id = update.effective_chat.id

    if text == "/start":
        await bot.send_message(
            chat_id=chat_id,
            text=(
                "Welcome to Trusted Bot!\n\n"
                "Available commands:\n"
                "/login - Connect your Telegram to your account\n"
                "/link <email> - Link this chat to your account\n"
                "/logoff - Disconnect Telegram from your account\n"
                "/help - Show this message"
            )
        )
    elif text == "/help":
        await bot.send_message(
            chat_id=chat_id,
            text=(
                "Available commands:\n"
                "/start - Welcome message\n"
                "/login - Get login link\n"
                "/link <email> - Link this chat to your account\n"
                "/logoff - Disconnect Telegram from your account\n"
                "/help - This message"
            )
        )
    elif text.startswith("/login"):
        await bot.send_message(
            chat_id=chat_id,
            text=(
                f"Visit {BASE_URL}/login to log in to your account.\n\n"
                f"After logging in, use /link youremail@example.com to connect this chat."
            )
        )
    elif text.startswith("/link"):
        parts = text.split(maxsplit=1)
        if len(parts) < 2:
            await bot.send_message(
                chat_id=chat_id,
                text="Usage: /link youremail@example.com"
            )
            return
        email = parts[1].strip()
        from auth import authenticate_user, link_telegram
        user = authenticate_user(email, "")
        if not user:
            from auth import get_user_by_chat_id as get_by_chat
            user = get_by_chat(str(chat_id))
            if user:
                link_telegram(user, str(chat_id))
                await bot.send_message(
                    chat_id=chat_id,
                    text="This chat is already linked to your account."
                )
                return
            await bot.send_message(
                chat_id=chat_id,
                text="No account found with that email. Sign up at " + BASE_URL
            )
            return
        from auth import authenticate_user as auth_user
        await bot.send_message(
            chat_id=chat_id,
            text="Please log in on the web first, then use /link with your email."
        )
    elif text.startswith("/logoff"):
        user = get_user_by_chat_id(str(chat_id))
        if user:
            unlink_telegram(str(chat_id))
            await bot.send_message(
                chat_id=chat_id,
                text="Your Telegram account has been disconnected."
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text="Your Telegram is not linked to any account."
            )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text="Unknown command. Use /help to see available commands."
        )
