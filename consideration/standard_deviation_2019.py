#!/usr/bin/env python3
# coding: utf-8

# 競走馬を馬名から強さに変換
import csv
for i in range(1,140):
  csvRow = []
  target_horse = []
  with open('./csv_2019/2019_race'+str(i)+'.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      target_horse.append(row[0])
    csvRow.append(target_horse[0])
  with open('./csv/strength_float.csv') as f:
    reader = csv.reader(f)
    index = 0 
    l = [row for row in reader]
    for k in range(0,len(l)):
      if l[k][0] in target_horse:
        csvRow.append(l[k][1])

  csvFile = open('./csv_2019/2019_race'+str(i)+'.csv', 'wt', newline='', encoding='utf-8')
  writer = csv.writer(csvFile)
  try:
    for num in range(0,len(csvRow)):
      array = []
      array.append(csvRow[num])
      writer.writerow(array)
  finally:
    csvFile.close()
