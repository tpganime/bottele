from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7629751514:AAEIDbsgITKeNWcEWldcoYmQIpURIDyQLbo"  # Replace with your bot token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "🔴 1k 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗥𝘀    -    300✅\n\n"
        "🔴 𝐅𝐮𝐥𝐥 𝐌𝐨𝐧𝐢𝐭𝐢𝐳𝐚𝐭𝐢𝐨𝐧  𝐑𝐬  -   750✅\n\n"
        "Demo Available\n"
        "100 subscribe 40 rupees\n\n"
        "🔴 10𝗞 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗥𝘀    -    580✅\n\n"
        "REAL WORK NOT FAKE"
    )

    keyboard = [
        [InlineKeyboardButton("WhatsApp Me", url="https://wa.me/91671702868")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(message_text, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
