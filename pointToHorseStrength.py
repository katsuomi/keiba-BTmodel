#!/usr/bin/env python3
# coding: utf-8

import csv

# 馬名:初期値(0)の辞書
pp_dict = {}

# pp_dictのtotal値
pp_total = 0

# 馬名:初期値(1)の辞書
result_dict = {}

# 選ばれた馬の対戦表(計算量を減らすために)
horse_competition_table = []

# 渡ってきた配列に関して、勝敗表を返す
# 引数の例: array = ['アーモンドアイ','サートゥルナーリア']
# 返り値の例: [0,2,2] この場合、0勝2敗で、合計2戦していることを表すことを表す
def match_result(array):
  match_result = [0,0,0]
  with open('./point.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    l_in = [s for s in l if array[0] and array[1] in s]
    for x in range(0,len(l_in)):
      if l_in[x][0] == array[0] and l_in[x][1] == array[1]:
        match_result[0] = (match_result[0] + int(l_in[x][2]))
      if l_in[x][1] == array[0] and l_in[x][0] == array[1]:
        match_result[1] = (match_result[1] + int(l_in[x][2]))

  match_result[2] = match_result[0] + match_result[1]
  return match_result

# 渡ってきた配列に関して、BTモデルより、強さを測定する(1)
# 引数の例 ['アーモンドアイ','サートゥルナーリア',0,2,2]
def calculate_btmodel_first(array):
  r = array[4] / (result_dict[array[0]] + result_dict[array[1]])
  return r

# 渡ってきた配列に関して、BTモデルより、強さを測定する(2)
# 引数の例 'アーモンドアイ'
def calculate_btmodel_second(horse_name):
  p = pp_dict[horse_name] / pp_total 
  return p


# resultに馬名:初期値(1)の辞書を作成
csvfile = open('./csv/allHorses.csv')
for row in csv.reader(csvfile):
  result_dict[row[0]] = 1
  pp_dict[row[0]] = 0
  

for k in range(0,15):
  csvfile = open('./csv/allHorses.csv')
  for row in csv.reader(csvfile):
    # row[0] は、選ばれた馬
    tmp_result = 0
    tmp_total_win_count = 0
    with open('./csv/horseCompetitionTable.csv') as f:
      reader2 = csv.reader(f)
      l = [row2 for row2 in reader2]
      l_in = [s for s in l if row[0] in s[0]]
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

  csvfile = open('./csv/allHorses.csv')
  for row in csv.reader(csvfile):
    result_dict[row[0]] = calculate_btmodel_second(row[0])

  pp_total = 0

csvFile = open("./csv/strength.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
  for k, v in result_dict.items():
    csvRow = []
    csvRow.append(k)
    csvRow.append(v)
    writer.writerow(csvRow)
finally:
  csvFile.close()
