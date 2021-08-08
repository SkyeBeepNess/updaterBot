import time
import config
import logging
import telegram
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, PicklePersistence
#skye_BeepNess
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
	updater = Updater("1410913727:AAHS0MygZhyD_I_FI3OHUYLW-pWg3y9OTR0", use_context=True)
	dispatcher = updater.dispatcher

	def clone(update, context):
		if update.effective_message.chat_id == 208339045:
			ssh = update.effective_message.text.split(' ')[1]
			
			x = subprocess.run(['git', 'clone', ssh], cwd="/home/beepuser/Documents/bots/", capture_output=True)
			
			#context.bot.send_message(update.effective_message.chat_id, x.stdout.decode(), parse_mode='HTML')
			context.bot.send_message(update.effective_message.chat_id, "Done!", parse_mode='HTML')
		else:
			context.bot.send_message(update.effective_message.chat_id, "It seems like you aren't allowed to do that", parse_mode='HTML')



	def pull(update, context):
		if update.effective_message.chat_id == 208339045:
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			x = subprocess.run(['git', 'pull'], cwd=PATH_OF_GIT_REPO, capture_output=True)
			
			context.bot.send_message(update.effective_message.chat_id, x.stdout.decode(), parse_mode='HTML')
			context.bot.send_message(update.effective_message.chat_id, "Everything is up to date now!", parse_mode='HTML')
		else:
			context.bot.send_message(update.effective_message.chat_id, "It seems like you aren't allowed to do that", parse_mode='HTML')

	def restart(update, context):
		if update.effective_message.chat_id == 208339045:
			lz={}
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			pidof = subprocess.run(['pidof', 'python3'], capture_output=True)


			for i in pidof.stdout.decode().split(' '):
				pwdx = subprocess.run(['pwdx', i], capture_output=True)
				l = pwdx.stdout.decode().split("/")
				l.reverse()
				lz[l[0].strip()]=i	
				
			
			if rep in lz:
				killed = subprocess.run(['kill', '-2', lz[rep]], capture_output=True)
				msg = context.bot.send_message(update.effective_message.chat_id, "turning the bot off...", parse_mode='HTML')
				while rep in lz:
					lz=[]
					for i in pidof.stdout.decode().split(' '):
						pwdx = subprocess.run(['pwdx', i], capture_output=True)
						l = pwdx.stdout.decode().split("/")
						l.reverse()
						lz.append(l[0].strip())
				context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg['message_id'], text="the bot is now off!", parse_mode='HTML')
				restarted = subprocess.Popen(['python3', 'app.py'], cwd=PATH_OF_GIT_REPO)
				context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg['message_id'], text="restarting...", parse_mode='HTML')
				while rep not in lz:
					lz=[]
					pidof = subprocess.run(['pidof', 'python3'], capture_output=True)
					for i in pidof.stdout.decode().split(' '):
						pwdx = subprocess.run(['pwdx', i], capture_output=True)
						l = pwdx.stdout.decode().split("/")
						l.reverse()
						lz.append(l[0].strip())
				context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg['message_id'], text="the bot is up and runing! (it seems so anyway)", parse_mode='HTML')
			else: 
				context.bot.send_message(update.effective_message.chat_id, "you have to start the bot first!", parse_mode='HTML')


		else:
			context.bot.send_message(update.effective_message.chat_id, "It seems like you aren't allowed to do that", parse_mode='HTML')



	def kill(update, context):
		if update.effective_message.chat_id == 208339045:
			lz={}
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			pidof = subprocess.run(['pidof', 'python3'], capture_output=True)
			for i in pidof.stdout.decode().split(' '):
				pwdx = subprocess.run(['pwdx', i], capture_output=True)
				l = pwdx.stdout.decode().split("/")
				l.reverse()
				lz[l[0].strip()]=i	
				
			
			if rep in lz:
				killed = subprocess.run(['kill', '-2', lz[rep]], capture_output=True)
				msg = context.bot.send_message(update.effective_message.chat_id, "turning the bot off...", parse_mode='HTML')
				while rep in lz:
					lz=[]
					pidof = subprocess.run(['pidof', 'python3'], capture_output=True)
					for i in pidof.stdout.decode().split(' '):
						pwdx = subprocess.run(['pwdx', i], capture_output=True)
						l = pwdx.stdout.decode().split("/")
						l.reverse()
						lz.append(l[0].strip())
				context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg['message_id'], text="the bot is now off!", parse_mode='HTML')
			else: 
				context.bot.send_message(update.effective_message.chat_id, "this bot isn't running anyway", parse_mode='HTML')

		else:
			context.bot.send_message(update.effective_message.chat_id, "It seems like you aren't allowed to do that", parse_mode='HTML')



	def start(update, context):
		if update.effective_message.chat_id == 208339045:
			lz=[]
			rep = update.effective_message.text.split(' ')[1]
			PATH_OF_GIT_REPO = f'/home/beepuser/Documents/bots/{rep}'
			pidof = subprocess.run(['pidof', 'python3'], capture_output=True)
			for i in pidof.stdout.decode().split(' '):
				pwdx = subprocess.run(['pwdx', i], capture_output=True)
				l = pwdx.stdout.decode().split("/")
				l.reverse()
				lz.append(l[0].strip())
			if rep in lz:
				context.bot.send_message(update.effective_message.chat_id, "This bot is already running!", parse_mode='HTML')
			else: 
				try:
					subprocess.Popen(['python3', 'app.py'], cwd=PATH_OF_GIT_REPO)
					context.bot.send_message(update.effective_message.chat_id, "the bot is up and runing! (it seems so anyway)", parse_mode='HTML')
				except:
					context.bot.send_message(update.effective_message.chat_id, "something went HORRIBLY wrong....", parse_mode='HTML')

		else:
			context.bot.send_message(update.effective_message.chat_id, "It seems like you aren't allowed to do that", parse_mode='HTML')




	dispatcher.add_handler(CommandHandler('pull', pull)) 
	dispatcher.add_handler(CommandHandler('restart', restart))  
	dispatcher.add_handler(CommandHandler('clone', clone))  	
	dispatcher.add_handler(CommandHandler('kill', kill))  
	dispatcher.add_handler(CommandHandler('start', start))  




	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
