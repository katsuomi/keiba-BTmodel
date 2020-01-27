#!/usr/bin/env python3
# coding: utf-8

import csv

result = []

with open('./point.csv') as f:
  reader = csv.reader(f)
  l = [row for row in reader]
  for i in range(1, len(l)):
    if not [l[i][0],l[i][1]] in result:
      result.append([l[i][0],l[i][1]])


csvFile = open("./HorseCompetitionTable.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
  for row in result:
    csvRow = []
    csvRow.append(row[0])
    csvRow.append(row[1])
    writer.writerow(csvRow)
finally:
  csvFile.close()