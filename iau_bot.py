from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace with your bot token
TOKEN = "7923580511:AAG0ucSbJKhKK17X0LpTiIJWnsl923Aaz8M"

# Questions and answers for Islamic Azad University
chatbot_responses = {
    "سلام": "سلام! چطور می‌تونم کمکت کنم؟",
    "مهلت انتخاب واحد کیه؟": "تا 15 مهر وقت داری، ولی سایت رو چک کن!",
    "مشروطی چیه؟": "اگه معدلت زیر 12 بشه، مشروطی می‌گیری.",
    "شهریه چقدره؟": "بستگی به رشته داره، مثلاً مهندسی حدود 5 میلیون تومنه."
}

# Start command
def start(update, context):
    update.message.reply_text("سلام! من چت‌بات دانشگاه آزادم. سوالت چیه؟")

# Handle messages
def handle_message(update, context):
    user_message = update.message.text
    response = chatbot_responses.get(user_message, "سوالتو نفهمیدم، واضح‌تر بپرس!")
    update.message.reply_text(response)

# Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    print("Bot started!")
    updater.idle()

if __name__ == "__main__":
    main()