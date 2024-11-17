#4449728
from get_history import get_history
from find_Id import ent
import csv
import pandas as pd
from read_csv_3t import read_csv
from Frontend import graphics
from data_analys import rates, comp_sp
from Front_vv import front_v

graphics() #frotnend

data = [] # Грузим файлы
f = open("paths.txt", "r")
for x in f.readlines():
    data.append(x[:-1])
print(data)

arr_s, arr_h, arr_d = read_csv(*data[:3])
sprint = data[3:]
if len(sprint) > 3:
    sprint = arr_s["sprint_name"].to_list()
area = "Система.Таск-трекер"
print(sprint)



data_bar_main = []
summery_main = []

for s in sprint:
    data_bar_main.append(rates(s, arr_s, area, arr_h, arr_d))
    summery_main.append(comp_sp(s, arr_s, area, arr_h, arr_d))

front_v(data_bar_main, area, summery_main)



