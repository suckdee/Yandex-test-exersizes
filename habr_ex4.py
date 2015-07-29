# -*- coding: utf-8 -*-

import sys
import re
import math
from urllib.request import urlopen

"""
Реализовать функцию-генератор строки с таблицей умножения на число Х.
"""
def multiplication_table(x):
    res = [str(x) +"x" + str(a) + "=" + str(a*x) for a in range(10)]
    print ('\n'.join(res))

"""
Есть лог-файл какого-то чата. Посчитать «разговорчивость» пользователей
в нем в виде ник — количество фраз. Посчитать среднее число букв на участника чата.
"""
def chat_log_counter(filename):
    log_file = open(filename,"rU")
    result = {}
    for n in log_file.readlines():
        chat_member = re.search('\s(\w)+',n)
        member_nik = str(chat_member.group())
        if not member_nik in result:
            result[member_nik] = 0
        else:
            result[member_nik] = result[member_nik] + 1
    print (result)

def main():
    #multiplication_table(3)
    chat_log_counter("chat_log.txt")




if __name__ == '__main__':
  main()