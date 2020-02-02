#!/usr/bin/env python3
# coding: utf-8

# G1のレースの場合　
import csv
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://jra.jp/datafile/seiseki/replay/2019/g1.html')
bsObj = BeautifulSoup(html, "html.parser")
num = 114
for a in bsObj.find_all('a', href=re.compile("result")):
  g1_url = 'http://jra.jp' + a.get('href')
  html2 = urlopen(g1_url)
  bsObj2 = BeautifulSoup(html2, "html.parser")

  csvRow = []
  #レース名の取得
  race_name = bsObj2.findAll("span", {"class": "race_name"})[0].get_text().strip()
  csvRow.append(race_name)
  
  table = bsObj2.findAll("table", {"class": "basic"})[0]
  rows = table.findAll("tbody")
  for row in rows:
    for cell in row.findAll("td", {"class": "horse"}):
      csvRow.append(cell.get_text().strip())
  num_str = str(num)
  csvFile = open("./csv_2019/2019_race"+num_str+".csv", 'wt',newline='', encoding='utf-8')
  writer = csv.writer(csvFile)
  try:
    #改行コードが入ってたから改行を消す
    for x in range(len(csvRow)):
      csvRow2 = []
      csvRow2.append(csvRow[x])
      writer.writerow(csvRow2)
  finally:
    csvFile.close()
  num = num + 1
  