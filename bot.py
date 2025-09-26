import os
import telebot

# Get bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables!")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your BotHost bot 🤖")

# /pricing command
@bot.message_handler(commands=['pricing'])
def send_pricing(message):
    text = (
        "🔴1k 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗥𝘀    -    300✅\n\n"
        "🔴𝐅𝐮𝐥𝐥 𝐌𝐨𝐧𝐢𝐭𝐢𝐳𝐚𝐭𝐢𝐨𝐧  𝐑𝐬  -   750✅\n\n"
        "Demo Available\n"
        "100 subscribe 40 rupees\n\n"
        "🔴𝟭0𝗞 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗥𝘀    -    580✅\n\n"
        "REAL WORK NOT FAKE\n\n"
        "WhatsApp me  -  9671702868"
    )
    bot.reply_to(message, text)

# Echo any other text
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

print("Bot is running...")
bot.infinity_polling()
