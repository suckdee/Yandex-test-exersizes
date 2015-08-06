#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime
import shutil
import subprocess

"""
Скрипт который распихает все файлы и папки в этой директории
по месяцам в формате Название папки = месяц
"""

def order_files(source_dir):
  source_dir_path = os.path.abspath(source_dir)
  files = os.listdir(source_dir_path)
  for file in files:
     modifiedTime =  os.path.getmtime(source_dir_path + "\\" + file)
     month_dir = (datetime.fromtimestamp(modifiedTime).strftime("%Y-%b"))
     if not os.path.exists(source_dir + "\\" + month_dir):
      os.mkdir(source_dir_path + "\\" + month_dir)
     shutil.move(source_dir + "\\" + file, source_dir +"\\" + month_dir + "//" + file)


def main():
  args = sys.argv[1:]
  if not args:
    print ("usage: [--source dir]")
    sys.exit(1)

  source = ''
  if args[0] == '--source':
    source = args[1]
    del args[0:2]

  if source:
    order_files(source)

if __name__ == "__main__":
  main()
