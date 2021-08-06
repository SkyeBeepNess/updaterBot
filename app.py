import subprocess
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, PicklePersistence
#skye_BeepNess
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
	updater = Updater("1410913727:AAHS0MygZhyD_I_FI3OHUYLW-pWg3y9OTR0", use_context=True)
	dispatcher = updater.dispatcher


	def pull(update, context):
		if update.effective_message.chat_id == 208339045:
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			x = subprocess.run(['git', 'pull'], cwd=PATH_OF_GIT_REPO, capture_output=True)
			
			context.bot.send_message(update.effective_message.chat_id, x.stdout.decode(), parse_mode='HTML')
			context.bot.send_message(update.effective_message.chat_id, "hello world", parse_mode='HTML')
		else:
			context.bot.send_message(update.effective_message.chat_id, "YOU SHALL NOT PASS", parse_mode='HTML')

	def restart(update, context):
		if update.effective_message.chat_id == 208339045:
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			#x = subprocess.run(['pkill', '-9', '-f', 'app.py'], cwd=PATH_OF_GIT_REPO, capture_output=True)
			updater.stop()
			os.execl(sys.executable, sys.executable, *sys.argv)
			context.bot.send_message(update.effective_message.chat_id, x.stdout.decode(), parse_mode='HTML')
		else:
			print('wf')
			#context.bot.send_message(update.effective_message.chat_id, "YOU SHALL NOT PASS", parse_mode='HTML')




	dispatcher.add_handler(CommandHandler('pull', pull)) 
	dispatcher.add_handler(CommandHandler('restart', restart))    				  




	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
