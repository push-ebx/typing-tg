from env import BOT_TOKEN
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler


async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  try:
    if update.message.to_dict()['forward_from']:
      with open("Output.txt", "w") as text_file:
        text_file.write(str(update.message.to_dict()['forward_from']['id']))
  except Exception as e:
    print(e)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  try:
    with open("Output.txt", "w") as text_file:
      text_file.write('')
  except Exception as e:
    print(e)


bot = ApplicationBuilder().token(BOT_TOKEN).build()

bot.add_handler(MessageHandler(filters.FORWARDED, handler))
bot.add_handler(CommandHandler("stop", stop))

bot.run_polling()
