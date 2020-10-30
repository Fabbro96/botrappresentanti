import time
import telepot
import random

token = '1141255362:AAFuNozJwRPdp7NW4WK3HIed56u63fLWYtA'
bot = telepot.Bot(token)

def rispondi(msq):
    chat_id = msq['chat']['id']
    comando = msq['text']
    user = msq['from']['username']
    if comando == '/start':
        bot.sendMessage(chat_id, "Ciao {} e benvenuto nel bot dei rappresentanti di uniVR! Usa /help per visualizzare i comandi ".format(user))
    elif comando == '/help':
        bot.sendMessage(chat_id, "Usa il comando /univrnews per entrare nel canale ufficiale di UniVR\n\nUsa /univrnews Canale ufficiale dell'UniVR discord\n\nUsa /secondoannoinfo per entrare nel gruppo di informatica del secondo anno\n\nUsa /canaletech per entrare nel gruppo per parlare di tecnologia fra nerd\n\nUsa /rappresentanti per poter parlare con un rappresentante\n\n[DISCORD] Usa il comando /discord per entrare nel nostro canale discord")
    elif comando == '/univrnews':
        bot.sendMessage(chat_id, '@UniVRNews_bot')
    elif comando == '/discord':
        bot.sendMessage(chat_id, 'https://discord.gg/vgB5HDR')
    elif comando == '/canaletech':
        bot.sendMessage(chat_id, 'https://bit.ly/2Sj8zrn')
    elif comando == '/secondoannoinfo':
        bot.sendMessage(chat_id, 'https://bit.ly/3ilDrlt')
    elif comando == '/rappresentanti':
        bot.sendMessage(chat_id, 'Vuoi contattare i rappresentanti di /informatica, /biotecnologie o /matematica?')
    elif(comando == '/informatica'):
        bot.sendMessage(chat_id,'Contatta @CallMeZeta, @Fabbrox oppure @richitosi')
    elif(comando == '/matematica'):
        bot.sendMessage(chat_id,'Contatta qualcuno, boh')
    elif(comando == '/biotecnologie'):
        bot.sendMessage(chat_id,'Contatta qualcuno, boh')
bot.message_loop(rispondi)
while 1:
    time.sleep(10)

