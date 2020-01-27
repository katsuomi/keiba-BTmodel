#!/usr/bin/env python3
# coding: utf-8

import csv

# 馬名:初期値(0)の辞書
r_dict = {}

# 馬名:初期値(0)の辞書
pp_dict = {}

# 馬名:初期値(0)の辞書
p_dict = {}

# 馬名:初期値(1)の辞書
result_dict = {}


# 渡ってきた配列に関して、勝敗表を返す
# 引数の例: array = ['アーモンドアイ','サートゥルナーリア']
# 返り値の例: [0,2,2] この場合、0勝2敗で、合計2戦していることを表すことを表す
def match_result(array):
  match_result = [0,0,0]
  with open('./point.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    for x in range(0,len(l)):
      if l[x][0] == array[0] and l[x][1] == array[1]:
        match_result[0] = (match_result[0] + int(l[x][2]))
      if l[x][1] == array[0] and l[x][0] == array[1]:
        match_result[1] = (match_result[1] + int(l[x][2]))

  match_result[2] = match_result[0] + match_result[1]
  return match_result

# 渡ってきた配列に関して、BTモデルより、強さを測定する(1)
# 引数の例 ['アーモンドアイ','サートゥルナーリア',0,2,2]
def calculate_btmodel_first(array):
  r = array[4] / (result_dict[array[0]] + result_dict[array[1]])
  return r




# 渡ってきた配列に関して、BTモデルより、強さを測定する(2)
# def calculate_btmodel_second(array):





# 渡ってきた配列に関して、BTモデルより、強さを測定する(3)
# def calculate_btmodel_third(array):


# resultに馬名:初期値(1)の辞書を作成
csvfile = open('./allHorses.csv')
for row in csv.reader(csvfile):
  result_dict[row[0]] = 1
  p_dict[row[0]] = 0
  pp_dict[row[0]] = 0
  r_dict[row[0]] = 0
  
csvfile = open('./allHorses.csv')
for row in csv.reader(csvfile):
  # row[0] は、選ばれた馬
  tmp_result = 0
  with open('./HorseCompetitionTable.csv') as f:
    reader2 = csv.reader(f)
    l = [row2 for row2 in reader2]
    for num in range(0,len(l)):
      if row[0] == l[num][0]:
        # elementは、選ばれた馬と戦う側の相手馬を格納している配列
        element = [l[num][0],l[num][1]]
        # 試合結果 ['アーモンドアイ','サートゥルナーリア',0,2,2]を格納
        match_result_array = [l[num][0],l[num][1],match_result(element)[0],match_result(element)[1],match_result(element)[2]]
        tmp_result += calculate_btmodel_first(match_result_array)
  r_dict[row[0]] = tmp_result


print(r_dict)


# const result = [1, 1, 1];

# const calc = result => {
#   const r1 = 10 / (result[0] + result[1]) + 10 / (result[0] + result[2]);
#   const r2 = 10 / (result[1] + result[0]) + 10 / (result[1] + result[2]);
#   const r3 = 10 / (result[2] + result[0]) + 10 / (result[2] + result[1]);

#   const pipi1 = 7 / r1;
#   const pipi2 = 9 / r2;
#   const pipi3 = 14 / r3;

#   let pi1 = (3 * pipi1) / (pipi1 + pipi2 + pipi3);
#   let pi2 = (3 * pipi2) / (pipi1 + pipi2 + pipi3);
#   let pi3 = (3 * pipi3) / (pipi1 + pipi2 + pipi3);
#   pi1 = pi1 * 10000000;
#   pi1 = Math.round(pi1);
#   pi1 = pi1 / 10000000;
#   pi2 = pi2 * 10000000;
#   pi2 = Math.round(pi2);
#   pi2 = pi2 / 10000000;
#   pi3 = pi3 * 10000000;
#   pi3 = Math.round(pi3);
#   pi3 = pi3 / 10000000;
#   result[0] = pi1;
#   result[1] = pi2;
#   result[2] = pi3;
#   return result;
# };

# const result1 = calc(result)

# const result2 = calc(result1)

# const result3 = calc(result2)

# const result4 = calc(result3)

# const result5 = calc(result4)

# const result6 = calc(result5)

# const result7 = calc(result6)

# const result8 = calc(result7)

# const result9 = calc(result8)

# const result10 = calc(result9)

# const result11 = calc(result10)

# const result12 = calc(result11)

# const result13 = calc(result12)

# const result14 = calc(result13)

# const result15 = calc(result14)

# const result16 = calc(result15)

# const result17 = calc(result16)

# const result18 = calc(result17)

# const result19 = calc(result18)

# const result20 = calc(result19)

# const result21 = calc(result20)

# const result22 = calc(result21)

# const result23 = calc(result22)

# const result24 = calc(result23)

# const result25 = calc(result24)

# const result26 = calc(result25)

# const result27 = calc(result26)

# const result28 = calc(result27)

# const result29 = calc(result28)

# const result30 = calc(result29)
