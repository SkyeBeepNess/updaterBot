import subprocess
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, PicklePersistence

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def pull(update, context):
	if update.effective_message.chat_id == 208339045:
		rep = update.effective_message.text.split(' ')[1]
		PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
		x = subprocess.run(['git', 'pull'], cwd=PATH_OF_GIT_REPO, text=True)
		
		context.bot.send_message(update.effective_message.chat_id, x, parse_mode='HTML')







def main():


	updater = Updater("1410913727:AAHS0MygZhyD_I_FI3OHUYLW-pWg3y9OTR0", use_context=True)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('pull', pull))    				  




	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
