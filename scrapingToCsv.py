#!/usr/bin/env python3
# coding: utf-8

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

for num in range(1, 113):
    if num > 99:
        num_str = str(num)
    elif num > 9:
        num_str = '0' + str(num)
    else:
        num_str = '00' + str(num)

    html = urlopen(
        'http://jra.jp/datafile/seiseki/replay/2014/'+num_str+'.html')
    bsObj = BeautifulSoup(html, "html.parser")

    table = bsObj.findAll("table", {"bgcolor": "#BABABA"})[0]
    rows = table.findAll("tr")

    csvFile = open("./keiba"+str(num)+".csv", 'wt',
                   newline='', encoding='utf-8')
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
