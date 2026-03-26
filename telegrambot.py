import telebot
import os 
from dotenv import load_dotenv
load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
sent_messages = {}

@bot.message_handler(commands = ['start'])
def greet(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Go to our website")
    markup.add(btn1)
    btn2 = telebot.types.KeyboardButton("Delete text")
    btn3 = telebot.types.KeyboardButton("Motivate")
    markup.row(btn2,btn3)

    file = open("Hora de aventura.jpg","rb")
    bot.send_photo(message.chat.id,file,reply_markup=markup)
    bot.send_message(message.chat.id,f"Hello {message.from_user.first_name} {message.from_user.last_name}",reply_markup=markup)
    

@bot.message_handler(commands =['help'])
def give_help(message):
    bot.send_message(message.chat.id, f"<b>Okay.... </b> (<em><u>your id is btw {message.from_user.id})</u></em>",parse_mode='html')

@bot.message_handler(content_types=['text'])
def handling(message):
    
    if message.text == "Go to our website":
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton("Website 😎", url = "https://www.wildberries.ru/")
        markup.row(btn1)
        bot.send_message(message.chat.id, "Click on the link below!",reply_markup=markup)
    elif message.text == "Delete text":
        markup = telebot.types.InlineKeyboardMarkup()
        btn2 = telebot.types.InlineKeyboardButton("But Are you sure 🤐?", callback_data="confirm_delete")
        markup.row(btn2)
        sent = bot.send_message(message.chat.id, "As you wish", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: None)  
        sent_messages[message.chat.id] = sent.message_id
    elif message.text == "Motivate":
        bot.send_message(message.chat.id,"Send me your picture now.")
        
@bot.message_handler(content_types=['photo'])
def get_new_text(message):
    bot.reply_to(message,"What a beautiful picture")
@bot.callback_query_handler(func = lambda callback : True)
def callback_message(callback):
    if callback.data == "confirm_delete":
        msg_id = sent_messages.get(callback.message.chat.id)
    if msg_id:
        bot.delete_message(callback.message.chat.id, msg_id)
        bot.send_message(callback.message.chat.id, "<b>Successfully deleted!</b>", parse_mode='html')
    
bot.infinity_polling()