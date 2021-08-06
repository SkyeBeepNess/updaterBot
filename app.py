import subprocess
import telegram
import logging
import time
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
			pidof = subprocess.run(['pidof', 'python3'], capture_output=True)
			for i in pidof.stdout.decode().split(' '):

				pwdx = subprocess.run(['pwdx', i], capture_output=True)
				l = pwdx.stdout.decode().split("/")
				l.reverse()
				lz = l[0].strip()
			
				if lz == rep:
					killed = subprocess.run(['kill', '-2', i], capture_output=True)
					context.bot.send_message(update.effective_message.chat_id, "turning the bot off...", parse_mode='HTML')
					time.sleep(10)
					restarted = subprocess.Popen(['python3', 'app.py'], cwd=PATH_OF_GIT_REPO, capture_output=True)
					#context.bot.send_message(update.effective_message.chat_id, restarted.stdout.decode(), parse_mode='HTML')
					context.bot.send_message(update.effective_message.chat_id, "the bot is up and runing! (it seems so anyway)", parse_mode='HTML')
					break
				else: 
					print('nope')

			context.bot.send_message(update.effective_message.chat_id, pidof.stdout.decode(), parse_mode='HTML')
		else:
			print('wf')
			#context.bot.send_message(update.effective_message.chat_id, "YOU SHALL NOT PASS", parse_mode='HTML')




	dispatcher.add_handler(CommandHandler('pull', pull)) 
	dispatcher.add_handler(CommandHandler('restart', restart))    				  




	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
