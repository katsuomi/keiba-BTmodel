#!/usr/bin/env python3
# coding: utf-8

import csv

result = []
with open('./point.csv') as f:
  reader = csv.reader(f)
  l = [row for row in reader]
  for x in range(0,len(l)):  
    if 'none' != l[x][0] and 'none' != l[x][1]:
      result.append([l[x][0],l[x][1],l[x][2]])

csvFile = open("./point.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
  for i in range(0,len(result)):
    csvRow = []
    csvRow.append(result[i][0])
    csvRow.append(result[i][1])
    csvRow.append(result[i][2])
    writer.writerow(csvRow)
finally:
  csvFile.close()
