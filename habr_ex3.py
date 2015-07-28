# -*- coding: utf-8 -*-

import sys
import re
import math
from urllib.request import urlopen

"""
Разработать программу «массовой закачки» доменов URL-ов из файла urls.txt
"""
def mass_domains(file_with_urls):
    input_file = open(file_with_urls,'rU')
    for url in input_file.readlines():
        domain_name = re.search(r'[\w]+[.]+[\w]+',url)
        print(domain_name.group())

"""
Разработать программу, скачивающую страницу по указанному URL.
"""
def web_page_download(url,filename):
    out_file = open(filename,"w")
    page = urlopen(url)
    print (page.read())
    out_file.write(str(page.read()))
    out_file.close()

"""
Написать программу, которая получив на входе произвольный список удалит из него все повторяющиеся элементы.
"""

def remove_repeated_1(list):
    result = []
    for n in list:
        if not n in result:
            result.append(n)
    print (result)

def remove_repeated_2(list):
    print (set(list))


def main():
    mass_domains("urls.txt")
    web_page_download("http://ya.ru","downloaded_page.html")
    remove_repeated_1([-1, -1, -1, 1, 2, 3, 4, 5, 6, 7, 8, 4, 10, 11])
    remove_repeated_2([-1, -1, -1, 1, 2, 3, 4, 5, 6, 7, 8, 4, 10, 11])



if __name__ == '__main__':
  main()