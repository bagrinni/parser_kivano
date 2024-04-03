# from bs4 import BeautifulSoup as Bs
# import requests
# import csv

# URL = 'https://enter.kg/computers/noutbuki_bishkek'
    
# def parser():
#     response = requests.get(url = URL)
#     soup = Bs(response.content,'html.parser')
#     items = soup.find_all('div', class_ = "product vm-col vm-col-1")
#     new_list = []
#     for i in items:
#         try:
#             new_list.append({'название':i.find('span',class_ = 'prouct_name').get_text(strip = True),
#                             'цена':i.find('span', class_ = 'price').get_text(strip = True),
#                              'изображение': i.find('a', class_ = 'product-image-link').find('img').get('src')
#                             })
#         except Exception as error:
#             print(f'Ошибка --{error}')

#     with open('output.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=['название', 'цена', 'изображение'])
#         writer.writeheader()
#         writer.writerows(new_list)

#     return new_list

# print(parser())


# from bs4 import BeautifulSoup as Bs
# import requests
# import csv

# URL = 'https://www.kivano.kg/planshety'
    
# def parser():
#     response = requests.get(url = URL)
#     soup = Bs(response.content,'html.parser')
#     items = soup.find_all('div', class_ = "item product_listbox oh")
#     new_list = []
#     for i in items:
#         try:
#             new_list.append({'название':i.find('div',class_ = 'listbox_title oh').get_text(strip = True),
#                             'цена':i.find('div', class_ = 'listbox_price text-center').get_text(strip = True),
#                              'изображение': i.find('div', class_ = 'listbox_img pull-left').find('img').get('src')
#                             })
#         except Exception as error:
#             print(f'Ошибка --{error}')

#     with open('kivano.txt', 'w', encoding='utf-8') as file:
#         for item in new_list:
#             file.write(f"Название: {item['название']}\nЦена: {item['цена']}\nИзображение: {item['изображение']}\n\n")

#     return new_list

# print(parser())



import telebot
import requests
from bs4 import BeautifulSoup


TOKEN = '6996194767:AAGNccCPWwrpplVbqmrw8n-sFgcPx77ji28'


bot = telebot.TeleBot(TOKEN)


def parse_currency():
    url = 'https://www.example.com'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим и извлекаем нужные данные (например, курс валюты)
    currency_data = soup.find('div', class_='currency-info').get_text()
    return currency_data

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку, чтобы получить курс валюты.')

# Обработчик нажатия кнопки
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Курс валюты':
        currency_info = parse_currency()
        bot.send_message(message.chat.id, f'Курс валюты: {currency_info}')

# Запуск бота
bot.polling()
    