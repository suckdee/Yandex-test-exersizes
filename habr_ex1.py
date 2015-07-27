# -*- coding: utf-8 -*-

import sys
import re
import math

"""
Составить программу расчета гипотенузы прямоугольного треугольника.
Длина катетов запрашивается у пользователя.
"""
def triangle_hypotenuse():
    katet1 = int(input("Введите длину первого катета"))
    katet2 = int(input("Введите длину второго катета"))
    hypotenus = math.sqrt(katet1 ** 2 + katet2 ** 2)
    print ("Длина гепотинузы равна: " + str(hypotenus))
    return hypotenus

"""
Составить программу вывода таблицы умножения на число M.
Таблица составляется от M * a, до M * b, где M, a, b
запрашиваются у пользователя. Вывод должен осуществляется
в столбик, по одному примеру на строку в следующем виде (например):
5 х 4 = 20
5 х 5 = 25
"""
def multiplication_table():
    m = int(input("Введите число M"))
    a = int(input("Введите число a"))
    b = int(input("Введите число b"))
    if a < b:
        for n in range(a,b):
            print (str(m) + "x" + str(n) +  "=" + str(m*n))
    else:
        print "Число a должно быть меньше числа b"



def main():
    triangle_hypotenuse()
    multiplication_table()


if __name__ == '__main__':
  main()