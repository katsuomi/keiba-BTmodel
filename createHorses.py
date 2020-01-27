#!/usr/bin/env python3
# coding: utf-8

import csv

result = []

with open('./point.csv') as f:
  reader = csv.reader(f)
  l = [row for row in reader]
  for i in range(1, len(l)):
    if not l[i][0] in result:
      result.append(l[i][0])
    if not l[i][1] in result:
      result.append(l[i][1])

csvFile = open("./allHorses.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
  for row in result:
    csvRow = []
    csvRow.append(row)
    writer.writerow(csvRow)
finally:
  csvFile.close()