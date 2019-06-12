from telegram.ext import Updater, CommandHandler
import logging
import serial

updater = Updater(token='899444561:AAF3zDczDPXSJRQYypp6JortNNNTDGZQjFM')
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a flower, you can ask how I'm doing by typing /status")

def status(bot, update):
    ser = serial.Serial('/dev/cu.usbmodem144101')
    ser_bytes = ser.readline()
    line = ser_bytes.decode('utf-8')
    bot.send_message(chat_id=update.message.chat_id, text=line)
    ser.close()

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
status_handler = CommandHandler('status', status)
dispatcher.add_handler(status_handler)
updater.start_polling()
