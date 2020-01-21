#!/usr/bin/env python3
# coding: utf-8

import csv
with open('./keiba1.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    for num in range(1, 21):
        for num2 in range(num+1, 21):
            result_num = [l[num][3], l[num2][3], 1]
            print(result_num)
