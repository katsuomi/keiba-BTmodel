#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import csv
import matplotlib.pyplot as plt
 
# グラフの表示

#平均
mean = []
#中央値
median = []
#分散
variance = []
#標準偏差
stdev = []

for i in range(1,2):
  with open('./csv_2019/2019_race'+str(i)+'.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      print(row[0])






# # 折れ線グラフを出力
# left = np.array([1, 2, 3, 4, 5])
# height = np.array([100, 300, 200, 500, 400])
# plt.plot(left, height, linestyle="solid")
# plt.show()
# # 折れ線グラフを出力
# left = np.array([1, 2, 3, 4, 5])
# height = np.array([100, 300, 200, 500, 400])
# plt.plot(left, height/2, linestyle="dashed")
# plt.show()
# # 折れ線グラフを出力
# left = np.array([1, 2, 3, 4, 5])
# height = np.array([100, 300, 200, 500, 400])
# plt.plot(left, height/3, linestyle="dashdot")
# plt.show()
# # 折れ線グラフを出力
# left = np.array([1, 2, 3, 4, 5])
# height = np.array([100, 300, 200, 500, 400])
# plt.plot(left, height/4, linestyle="dotted")
# plt.show()
