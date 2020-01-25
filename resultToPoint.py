#!/usr/bin/env python3
# coding: utf-8

import csv

with open('./result.csv') as f:
    reader = csv.reader(f)
    index = 0 
    l = [row for row in reader]
    for x in range(0,len(l)):
        for y in range(index+1,len(l)):
            if l[x][0] == l[y][0] and l[x][1] == l[y][1]:
                l[y][0] = "none"
                l[x][2] = str(int(l[x][2]) + 1)
        index += 1

    # 買った馬の表示 l[0][0]
    # 負けた馬の表示 l[0][1]
    # 数値の表示 l[0][2]
csvFile = open("./point.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in l:
        csvRow = []
        csvRow.append(row[0])
        csvRow.append(row[1])
        csvRow.append(row[2])
        writer.writerow(csvRow)
finally:
    csvFile.close()
