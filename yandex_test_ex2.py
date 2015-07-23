# -*- coding: utf-8 -*-
"""
В системе авторизации есть ограничение логин должен
начинаться с латинской буквы, состоять из латинских букв
цифр, точки и минуса, но заканчиваться только латинской
буквой или цифрой; минимальная длина логина — один символ,
максимальная — 20. Напишите код, проверяющий соответствие
входной строки этому правилу. Придумайте несколько способов
решения задачи и сравните их.
"""
import re

def validation_one(login):
    is_valid = True
    if 0 < len(login) <= 20 and login[0].isalpha() and (login[-1].isalpha() or login[-1].isdigit()):
        for c in login.lower()[1:-1]:
            if not c.isalpha() and not c.isdigit() or c in ['.','-']:
                is_valid =False
                print ("Логин должен содержать только английские буквы,цифры и смволы точек и тире")
                break
    else:
        print ("Логин не соответвует длине или начинается не с латинской буквы или цифры")
        is_valid =False
    if is_valid == True:
        print ("Логин принят")

def validation_two(login):
    pattern = re.compile("^[A-Za-z][A-Za-z0-9.-]{0,19}[A-Za-z0-9]?$")
    if pattern.match(login):
        print ("Логин принят")
    else:
        print("Логин должен содержать только английские буквы,цифры и смволы точек и тире")


def main():
    validation_one("suckdee")
    validation_two("suckdee")


if __name__ == '__main__':
  main()