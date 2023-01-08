import sqlite3
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from random import randint
url = 'https://www.tripadvisor.ru/RestaurantSearch-g298484-Moscow_Central_Russia.html#EATERY_LIST_CONTENTS'
base_url = 'https://www.tripadvisor.ru'
response = HTMLSession()
html = response.get(url).text
urls = []
soup = BeautifulSoup(html,'html.parser')
contain = soup.find_all('div',class_="RfBGI")
for i in contain:
    a=i.select_one('a')['href']
    urls.append(base_url+a)
a=soup.find('div',class_='pageNumbers')
furls=[]
for i in range(2,7):
    g=a.find('a',{'data-page-number':f'{i}'})['href']
    furls.append(base_url+g)
for han in furls:
    html = response.get(han).text
    soup = BeautifulSoup(html, 'html.parser')
    contain = soup.find_all('div', class_="RfBGI")
    for i in contain:
        a = i.select_one('a')['href']
        urls.append(base_url + a)
args = []
id=0
count=0
for i in urls:
    try:
        id+=1
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find('h1',{"data-test-target":"top-info-header"}).text
        adress_ = soup.find('a',class_='AYHFM').find_next('a',class_='AYHFM').text
        phone_ = soup.find('span',class_="AYHFM").text
        rate_ = soup.find('span',class_='ZDEqb').text
        range_money_ = soup.find('div',class_='SrqKb').text
        type_cook_ = soup.find('div',class_='SrqKb').find_next('div',class_='SrqKb').text
        photo_one_ = soup.find('div',class_="prw_rup prw_common_basic_image photo_widget large landscape").select_one('img')['data-lazyurl']
        photo_two_ = soup.find('div', class_="prw_rup prw_common_basic_image photo_widget large landscape").find_next('div', class_="prw_rup prw_common_basic_image photo_widget large landscape").select_one('img')['data-lazyurl']
        time_ = soup.find('span',class_='mMkhr').find_next('span').find_next('span').find_next('span').text
        if time_==' Посмотреть время работы':
            time_='10:00 AM - 11:00 PM'
        a = randint(1,3)
        b = randint(1,2)
        budget_=0
        if a==1:
            budget_='эконом класс'
        elif a==2:
            budget_='стандарт класс'
        elif a==3:
            budget_='бюджет класс'
        type_= 0
        if b==1:
            type_='кафе'
        elif b==2:
            type_='ресторан'
        print(time_,budget_,type_)
    except:
        id-=1
        count+=1
    else:
        args.append((id,name_,adress_,phone_,rate_,range_money_,type_cook_,photo_one_,photo_two_,time_,budget_,type_))
print(count)
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
cursor.executemany("INSERT INTO app_restoran_restorans VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", args)
conn.commit()
conn.close()