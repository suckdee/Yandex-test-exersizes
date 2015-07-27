# -*- coding: utf-8 -*-

import sys
import re
import math

"""
Написать программу, выводящую заданную пользователем строку
как минимум в 3 разных кодировках. При этом писать вызов
метода encode() в программе можно только 1 раз.
"""
def string_encode():
    input_str = input("Введите строку: ")
    for enc in ["UTF-8","cp1251","koi8-r"]:
        print (input_str.encode(enc))

"""
Написать программу поиска самого длинного слова в строке, разделенной пробелами.
"""
def longest_word():
    input_str = input("Введите строку: ")
    words = input_str.split(" ")
    my_dict = {}
    for word in words:
        my_dict[word] = len(word)
    print (max(my_dict, key=my_dict.get))

"""
Написать программу декодирования телефонного номера для АОН.
По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
— Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
— Каждая значащая цифра повторяется минимум 2 раза
— Если в номере идут несколько цифр подряд, то для обозначения
«такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #
"""

def aon(phone_number):
    tel_without_noises = ''
    last_digit = ''
    final_number = ''

    for n in phone_number:
        if (len(tel_without_noises) == 0 ):
            tel_without_noises += n
        elif last_digit == n and tel_without_noises[-1] != n:
            tel_without_noises += n
        elif last_digit == n and tel_without_noises[-1] == n:
            tel_without_noises += '#'
        last_digit = n
    final_number = tel_without_noises
    print (final_number)


def main():
    string_encode()
    longest_word()
    aon(" 4434###552222311333661")


if __name__ == '__main__':
  main()