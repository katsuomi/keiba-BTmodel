#!/usr/bin/env python3
# coding: utf-8

# 標準偏差を表示
import csv
from statistics import mean, median,variance,stdev

for i in range(79,140):
  data = []
  csvRow = []
  target_strength = []
  with open('./csv_2019/2019_race'+str(i)+'.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      target_strength.append(row[0])
    csvRow.append(target_strength[0])
    target_strength.pop(0)
    
  for num in range(0,len(target_strength)):
    data.append(float(target_strength[num]) * 100000)

  csvRow.append("平均")
  csvRow.append(format(mean(data)))
  csvRow.append("中央値")
  csvRow.append(format(median(data)))
  csvRow.append("分散")
  csvRow.append(format(variance(data)))
  csvRow.append("標準偏差")
  csvRow.append(format(stdev(data)))
  csvFile = open('./csv_2019/2019_race'+str(i)+'.csv', 'wt', newline='', encoding='utf-8')
  writer = csv.writer(csvFile)
  try:
    for num in range(0,len(csvRow)):
      array = []
      array.append(csvRow[num])
      writer.writerow(array)
  finally:
    csvFile.close()
