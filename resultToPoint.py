#!/usr/bin/env python3
# coding: utf-8

import csv

result = []
with open('./result.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

csvFile = open("./point.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in l:
        csvRow = []
        csvRow.append(row)
        writer.writerow(csvRow)
finally:
    csvFile.close()
