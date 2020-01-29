#!/usr/bin/env python3
# coding: utf-8

import csv

result = []

csvfile = open('./csv/allHorses.csv')
for row in csv.reader(csvfile):
  with open('./csv/point.csv') as f:
    reader = csv.reader(f)
    l = [row2 for row2 in reader]
    result = [s for s in l if row[0] in s]
  csv_name = row[0]+'.csv'
  csvFile = open('./horse_point_csv/'+csv_name, 'wt', newline='', encoding='utf-8')
  writer = csv.writer(csvFile)
  try:
    for row in result:
      csvRow = []
      csvRow.append(row[0])
      csvRow.append(row[1])
      csvRow.append(row[2])
      writer.writerow(csvRow)
  finally:
    csvFile.close()