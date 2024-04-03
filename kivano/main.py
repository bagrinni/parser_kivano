import requests
from bs4 import BeautifulSoup as B
import csv

URL = 'https://www.kivano.kg/'


class Parser():
    def __init__(self,url:str,path:str) -> None:
        self.url = URL+url
        self.path = path


    def get_content(self):
        r = requests.get(self.url)
        s = B(r.content,'html.parser')
        items = s.find_all('div',class_ = 'item product_listbox oh')
        new_list = []
        for i in items:
            new_list.append({
                'title': i.find('div', class_='listbox_title oh').find('a').get_text(strip=True),
                'price': i.find('div', class_= 'listbox_price text-center').get_text(strip=True),
                'images': i.find('div', class_='listbox_img pull-left').find('img').get('src')
            })
        return new_list
   

    def save(self,products):
        with open(self.path, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Название', 'Цена', 'Изображение'])
            for i in products:
                writer.writerow([i['title'], i['price'], i['images']])
p = Parser(
    url = input("Введите категорию:"),
    path= "{}.csv".format(input("введите название файла:"))
)
a = p.get_content()
p.save(a)