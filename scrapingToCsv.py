#!/usr/bin/env python3
# coding: utf-8

import csv
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html2 = urlopen(
    'http://jra.jp/datafile/seiseki/g1/hopeful/result/hopeful2018.html')
bsObj2 = BeautifulSoup(html2, "html.parser")

table = bsObj2.findAll("table", {"class": "striped"})[0]
rows = table.findAll("tr")
csvFile = open("./keiba682.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())

        # 改行コードが入ってたから改行を消す
        for x in range(len(csvRow)):
            csvRow[x] = csvRow[x].replace('\n', '')

        writer.writerow(csvRow)
finally:
    csvFile.close()


# import csv
# import re
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# num = 627
# html = urlopen('http://jra.jp/datafile/seiseki/replay/2017/g1.html')
# bsObj = BeautifulSoup(html, "html.parser")
# for a in bsObj.find_all('a', href=re.compile("result")):
#     g1_url = 'http://jra.jp' + a.get('href')
#     html2 = urlopen(g1_url)
#     bsObj2 = BeautifulSoup(html2, "html.parser")

#     table = bsObj2.findAll("table", {"bgcolor": "#BABABA"})[0]
#     rows = table.findAll("tr")
#     num_str = str(num)
#     csvFile = open("./keiba"+num_str+".csv", 'wt',
#                    newline='', encoding='utf-8')
#     writer = csv.writer(csvFile)
#     try:
#         for row in rows:
#             csvRow = []
#             for cell in row.findAll(['td', 'th']):
#                 csvRow.append(cell.get_text())

#             # 改行コードが入ってたから改行を消す
#             for x in range(len(csvRow)):
#                 csvRow[x] = csvRow[x].replace('\n', '')

#             writer.writerow(csvRow)
#     finally:
#         csvFile.close()
#     num = num + 1


# G2 ~ G3のレースの場合、以下でOKだが、G1のレースは上記で実装　
# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# for num in range(1, 113):
#     if num > 99:
#         num_str = str(num)
#     elif num > 9:
#         num_str = '0' + str(num)
#     else:
#         num_str = '00' + str(num)

#     html = urlopen(
#         'http://jra.jp/datafile/seiseki/replay/2018/'+num_str+'.html')
#     bsObj = BeautifulSoup(html, "html.parser")

#     table = bsObj.findAll("table", {"class": "mainList"})[0]
#     rows = table.findAll("tr")

#     num2 = str(num+446)
#     csvFile = open("./keiba"+num2+".csv", 'wt', newline='', encoding='utf-8')
#     writer = csv.writer(csvFile)
#     try:
#         for row in rows:
#             csvRow = []
#             for cell in row.findAll(['td', 'th']):
#                 csvRow.append(cell.get_text())

#             # 改行コードが入ってたから改行を消す
#             for x in range(len(csvRow)):
#                 csvRow[x] = csvRow[x].replace('\n', '')

#             writer.writerow(csvRow)
#     finally:
#         csvFile.close()
