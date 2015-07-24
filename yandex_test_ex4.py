# -*- coding: utf-8 -*-
"""
Предположим, у нас есть access.log веб-сервера.
Как с помощью стандартных консольных средств найти
десять IP-адресов, от которых было больше всего
запросов? А как сделать это с помощью скрипта на Python?
"""
import sys
import re

def top10_ip_search(log_file):
    ip_address_counter ={}
    input_file = open(log_file,"r")
    for line in input_file:
        words = line.split(" ")
        ip_address = words[0]
        if not ip_address in ip_address_counter:
            ip_address_counter[ip_address] = 1
        else:
            ip_address_counter[ip_address] = ip_address_counter[ip_address] + 1
    top_ip_address = (sorted(ip_address_counter.items(),key=lambda x: x[1],reverse=True))
    print (top_ip_address[0:9])
    input_file.close()


def main():
    top10_ip_search("access_log.txt")


if __name__ == '__main__':
  main()