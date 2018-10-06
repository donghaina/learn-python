#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

import requests
import csv
import mysql.connector
import codecs


def connect_db():
    my_db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        db='douban'
    )
    return my_db


def insert_data(data_list):
    print(data_list)
    # list_tuples = [tuple(map(lambda x: x.encode('utf-8'), tup)) for tup in data]
    my_db = connect_db()
    print(my_db)
    my_cursor = my_db.cursor()
    print(my_cursor)
    # sql = "insert into top_250 (title,origin_title,star) values (%s,%s,%s)",
    sql = """insert into top_250 (title,origin_title,star) values (%s,%s,%s)""",
    # my_cursor.executemany(sql, data_list)
    tup = ('卡罗尔', 'Carol', 8.5)
    my_cursor.execute(sql, tup)
    my_db.commit()


def get_page(page):
    data_list = []
    url = 'https://movie.douban.com/top250?start={}'.format(page)
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    film_list_container = soup.find_all('ol', {'class': 'grid_view'})[0]
    film_list = film_list_container.find_all('li')

    for item in film_list:
        title_list = item.select('.item .info .hd a .title')
        star = item.select('.item .info .star .rating_num')[0].get_text()
        chinese_title = title_list[0].get_text()
        if len(title_list) == 1:
            origin_title = '无'
        else:
            origin_title = title_list[1].get_text()[2:].strip()
        film_item = (chinese_title, origin_title, star)
        data_list.append(film_item)
        with codecs.open('top_250.csv', 'a', 'utf-8') as my_file:
            my_writer = csv.writer(my_file)
            print(list(film_item))
            my_writer.writerow(list(film_item))

            # return data
            # print(data)
            # insert_data(data_list)


for i in range(0, 250, 25):
    get_page(i)
