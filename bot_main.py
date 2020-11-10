import time
import os

from telepot import Bot
from telepot.loop import MessageLoop

from dotenv import load_dotenv

# Loads .env file
load_dotenv()
# Inits TOKEN var with token value from .env
TOKEN = os.getenv('token')

bot = Bot(TOKEN)

# Command: \start -> Starts the bot
def start_handler(chat_id, user):
    bot.sendMessage(chat_id, 'Ciao {} e benvenuto nel bot dei rappresentanti di uniVR! Usa /help per visualizzare i comandi '.format(user))


# Command: \help -> Prints an help message on the general functions
def help_handler(chat_id):
    bot.sendMessage(chat_id, 'Usa il comando /univrnews per entrare nel canale ufficiale di UniVR\n\n' +
                    'Usa /univrnews Canale ufficiale dell\'UniVR discord\n\n' +
                    'Usa /secondoannoinfo per entrare nel gruppo di informatica del secondo anno\n\n' +
                    'Usa /canaletech per entrare nel gruppo per parlare di tecnologia fra nerd\n\n' +
                    'Usa /rappresentanti per poter parlare con un rappresentante\n\n' +
                    '[DISCORD] Usa il command /discord per entrare nel nostro canale discord')


# Command: \univrnews -> Link to the News channel
def univrnews_handler(chat_id):
    bot.sendMessage(chat_id, '@UniVRNews_bot')


# Command: \discord -> Link to our Discord server
def discord_handler(chat_id):
    bot.sendMessage(chat_id, 'https://discord.gg/vgB5HDR')


# Command: \canaletech -> Link to the Tech channel
def canaletech_handler(chat_id):
    bot.sendMessage(chat_id, 'https://bit.ly/2Sj8zrn')


# Command: \secondoannoinfo -> Link to the CS second year group
def secondoannoinfo_handler(chat_id):
    bot.sendMessage(chat_id, 'https://bit.ly/3ilDrlt')


# Command: \rappresentanti -> Prints an help message on how to contact Reps
def rappresentanti_handler(chat_id):
    bot.sendMessage(chat_id, 'Vuoi contattare i rappresentanti di /informatica, /biotecnologie o /matematica?')


# Command: \informatica -> CS Reps
def informatica_handler(chat_id):
    bot.sendMessage(chat_id,'Contatta @CallMeZeta, @Fabbrox oppure @richitosi')


# Command: \bioinformatica -> Bioinformatics Reps
def bioinformatica_handler(chat_id):
    bot.sendMessage(chat_id,'Contatta qualcuno, boh')


# Command: \matematica -> Mathematics Reps
def matematica_handler(chat_id):
    bot.sendMessage(chat_id,'Contatta qualcuno, boh')


# Command: \biotecnologie -> Biotechnologies Reps
def biotecnologie_handler(chat_id):
    bot.sendMessage(chat_id,'Contatta qualcuno, boh')


# Command: \ticket -> Opens a ticket that allows to submit an anonymous message to Reps
def ticket_handler(chat_id, user_id):
    # Id of the ticket handling group
    # Same as user_id for debug purpose
    th_chat_id = user_id

    # Sends a DM to the user who invokes the /ticket command
    bot.sendMessage(user_id, 'Scrivimi qual è il problema :)')

    # TODO Sulla carta è corretto, bisogna capire bene come funziona il getUpdates
    # Waits for answer (1 minute timeout)
    response = bot.getUpdates(timeout=60)

    # Sleeps then sends the answers to the ticket handling group
    for responses in response:
        bot.sendMessage(th_chat_id, responses['message']['text'])


# Main msg handler
def main_handler(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    user = msg['from']['username']

    if command == '/start':
        start_handler(chat_id, user)
    elif command == '/help':
        help_handler(chat_id)
    elif command == '/univrnews':
        univrnews_handler(chat_id)
    elif command == '/discord':
        discord_handler(chat_id)
    elif command == '/canaletech':
        canaletech_handler(chat_id)    
    elif command == '/secondoannoinfo':
        secondoannoinfo_handler(chat_id)
    elif command == '/rappresentanti':
        rappresentanti_handler(chat_id)    
    elif command == '/informatica':
        informatica_handler(chat_id)
    elif command == '/bioinformatica':
        bioinformatica_handler(chat_id)
    elif command == '/matematica':
        matematica_handler(chat_id)
    elif command == '/biotecnologie':
        biotecnologie_handler(chat_id)
    elif command == '/ticket':
        ticket_handler(chat_id, msg['from']['id'])


# Runs message loop listening for commands invocations
MessageLoop(bot, handle=main_handler).run_as_thread()
print('Polling...')

# Keeps the bot running
while 1:
    time.sleep(10)
