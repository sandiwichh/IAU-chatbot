from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من چت‌بات دانشگاه آزادم. سوالت چیه؟")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = chatbot_responses.get(user_message, "سوالتو نفهمیدم، واضح‌تر بپرس!")
    await update.message.reply_text(response)

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started!")
    app.run_polling()

if __name__ == "__main__":
    main()
