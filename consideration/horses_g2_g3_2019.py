#!/usr/bin/env python3
# coding: utf-8

# G2 ~ G3のレースの場合
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

for num in range(1, 114):
  if num > 99:
    num_str = str(num)
  elif num > 9:
    num_str = '0' + str(num)
  else:
    num_str = '00' + str(num)

  html = urlopen('http://jra.jp/datafile/seiseki/replay/2019/'+num_str+'.html')
  bsObj = BeautifulSoup(html, "html.parser")
  csvRow = []
  #レース名の取得
  race_name = bsObj.findAll("span", {"class": "race_name"})[0].get_text().strip()
  csvRow.append(race_name)
  table = bsObj.findAll("table", {"class": "basic"})[0]
  rows = table.findAll("tbody")
  for row in rows:
    for cell in row.findAll("td", {"class": "horse"}):
      csvRow.append(cell.get_text().strip())

  num2 = str(num)
  csvFile = open("./csv_2019/2019_race"+num2+".csv", 'wt', newline='', encoding='utf-8')
  writer = csv.writer(csvFile)
  try:
    for x in range(len(csvRow)):
      csvRow2 = []
      csvRow2.append(csvRow[x])
      writer.writerow(csvRow2)
  finally:
    csvFile.close()