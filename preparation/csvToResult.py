#!/usr/bin/env python3
# coding: utf-8

import csv

result = []

for i in range(1, 683):
    i_str = str(i)
    csv_name = 'keiba' + i_str+'.csv'
    with open('./race_csv/'+csv_name) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        for num in range(1, len(l)):
            for num2 in range(num+1, len(l)):
                result.append([l[num][3], l[num2][3], 1])

csvFile = open("./result.csv", 'wt', newline='', encoding='utf-8')
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


# for文で、配列が既に存在しているのかをチェックする。処理時間が長く、この方法は厳しい。
# import csv

# result = []

# with open('./keiba1.csv') as f:
#     reader = csv.reader(f)
#     l = [row for row in reader]
#     for num in range(1, len(l)):
#         for num2 in range(num+1, len(l)):
#             if len(result) == 0:
#                 result.append([l[num][3], l[num2][3], 1])
#             else:
#                 for i in range(0, len(result)):
#                     if result[i][0] == l[num][3] and result[i][1] == l[num2][3]:
#                         result[i][2] += 1
#                     else:
#                         result.append([l[num][3], l[num2][3], 1])

# print(result)
