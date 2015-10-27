# -*- coding: utf-8 -*-
 
#Libreria usada 
#https://github.com/eternnoir/pyTelegramBotAPI#a-simple-echo-bot
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
TOKEN = '' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['hola']) # Indicamos que lo siguiente va a controlar el comando '/hola'.
def command_hola(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message(cid,'Este es el comando /hola asi que Hola!! pronto aprendere a conversar!')
    
@bot.message_handler(commands=['chau']) # Indicamos que lo siguiente va a controlar el comando '/chau'
def command_chau(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Este es el comando /chau asi que Chau!! pronto aprendere a conversar!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

@bot.message_handler(content_types=['text'])
def text_handler(m): 
    cid = m.chat.id 
    if m.text == 'Harold':
        bot.send_message(cid,'Hola yo conozco a mi creador tu eres GUILLERMO')
    elif m.text == 'foto':
        bot.send_message(cid,'FOTO')
        photo = open('images/Bebe_borracho-300x225.jpg', 'rb')
        bot.send_photo(cid, photo)
        bot.send_photo(cid, "FILEID")
    elif m.text == 'encuesta':
        markup = types.ReplyKeyboardMarkup()
        markup.add('1', '2', '3')
        bot.send_message(cid, "Elegi un numero:", reply_markup=markup)
    elif m.text == '1':
        bot.send_message(cid,'uno')
        keyboardHide(cid)
    elif m.text == '2':
        bot.send_message(cid,'dos')
        keyboardHide(cid)
    elif m.text == '3':
        bot.send_message(cid,'tres')
        keyboardHide(cid)
    else :
        bot.send_message(cid,'No reconozco todas las palabras, escribi encuesta')
        
@bot.message_handler(content_types=['location']) 
def weather_location_handler(m): 
    cid = m.chat.id 
    bot.send_message(cid,m.location)
    bot.send_message(cid, 'Enviaste un mapa, yo estoy aqui')
    bot.send_location(cid,-32.891929,-68.839889)
        
############################################
#Funciones locales
def keyboardHide(cid):
    markup = types.ReplyKeyboardHide(selective=False)
    bot.send_message(cid, 'gracias por responder', reply_markup=markup)

#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
