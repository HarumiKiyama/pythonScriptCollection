# -*- coding: utf-8 -*-

import sys

import time

reload(sys)
sys.setdefaultencoding('utf8')
import re

import requests
from bs4 import BeautifulSoup

HOME_HTML = 'https://isekailunatic.wordpress.com/tsuki-ga-michibiku-isekai-douchuu/'


def get_soup(url):
    try:
        return BeautifulSoup(requests.get(url).content, 'html.parser')
    except:
        time.sleep(20)
        return get_soup(url)


def get_a_tag_list():
    home_soup = get_soup(HOME_HTML)
    res = []
    for a_tag in home_soup.find_all(href=re.compile('\d/prologue-')):
        res.append(a_tag.get('href'))
    for a_tag in home_soup.find_all(href=re.compile('chapter-\d')):
        res.append(a_tag.get('href'))
    return res


def get_one_chapter(url):
    chapter_soup = get_soup(url)
    res = chapter_soup.find('h1', class_='entry-title').get_text() + '\n'
    print res + 'completed'
    for p in chapter_soup.find('div', class_='entry-content').find_all('p'):
        if not p.find('a'):
            res += p.get_text() + '\n'
    return res


def write_book():
    for url in get_a_tag_list():
        with open('C:/Users/wwl/Desktop/tsuki.txt', 'a') as f:
            f.write(get_one_chapter(url))


if __name__ == '__main__':
    write_book()
