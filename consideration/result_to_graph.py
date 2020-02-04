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

length = []

for i in range(1,140):
  with open('./csv_2019/2019_race'+str(i)+'.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      mean.append(float(row[2]))
      median.append(float(row[4]))
      variance.append(float(row[6]))
      stdev.append(float(row[8]))

# 折れ線グラフを出力
for i in range(0,len(mean)):
  length.append(i)

left = np.array(length)
mean_height = np.array(mean)
median_height = np.array(median)
variance_height = np.array(variance)
stdev_height = np.array(stdev)
# plt.plot(left, mean_height, linestyle="solid", marker="o", color="red")
# plt.plot(left, median_height, linestyle="dashed", marker="o", color="blue")
plt.plot(left, variance_height, linestyle="dashdot", marker="o", color="orange")
# plt.plot(left, stdev_height, linestyle="dotted", marker="o", color="black")
plt.show()
