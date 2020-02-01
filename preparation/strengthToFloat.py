#!/usr/bin/env python3
# coding: utf-8

import csv
from decimal import Decimal

result = []

csvfile = open('./csv/strength_float.csv')
for row in csv.reader(csvfile):
  if 'E' in str(row[1]):
    result.append([row[0],0])
  else:
    result.append([row[0],Decimal(row[1])])
csvFile = open('./csv/strength_float.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
  for i in range(0,len(result)):
    csvRow = []
    csvRow.append(result[i][0])
    csvRow.append(result[i][1])
    writer.writerow(csvRow)
finally:
  csvFile.close()