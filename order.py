#!/usr/bin/env python3
# coding: utf-8

import csv

csvfile = open('./allHorses.csv')
for row in csv.reader(csvfile):
  # row[0] は、選ばれた馬
  tmp_result = 0
  tmp_total_win_count = 0
  with open('./horseCompetitionTable.csv') as f:
    reader2 = csv.reader(f)
    l = [row2 for row2 in reader2]
    l_in = [s for s in l if row[0] in s[0]]
    print(l_in)
    for num in range(0,len(l_in)):
      if row[0] == l_in[num][0]:
        # elementは、選ばれた馬と戦う側の相手馬を格納している配列
        element = [l_in[num][0],l_in[num][1]]
        # 試合結果 ['アーモンドアイ','サートゥルナーリア',0,2,2]を格納
        match_result_array = [l_in[num][0],l_in[num][1],match_result(element)[0],match_result(element)[1],match_result(element)[2]]
        tmp_result += calculate_btmodel_first(match_result_array)
        tmp_total_win_count += match_result(element)[0]
  if tmp_result != 0:
    pp_dict[row[0]] = tmp_total_win_count / tmp_result
    pp_total += pp_dict[row[0]]

