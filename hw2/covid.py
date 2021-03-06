# -*- coding: utf-8 -*-
"""covid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ozn6_Ss16P_AurHag6FrjrWxLqEFRq7h
"""

from google.colab import drive
drive.mount('/content/drive/')

path_covid = '/content/drive/MyDrive/ColabNotebooks/covidTrain.csv'

file = open(path_covid)

type(file)

import re

import csv

csvreader = csv.reader(file)

# extracting field names
header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
  rows.append(row)

dictt_covid = {}
for c in range(len(header)):
  val = []
  for r in range(len(rows)):
    val.append(rows[r][c])
  dictt_covid[header[c]] = val

dictt_covid

#Q1

age_covid = dictt_covid['age']

new_age = []
for val in age_covid:
  #print(val)
  
  if re.search(r'\s*\d{1,2}-\d{1,2}\s*',val):
    val_int = []
    #print(val)
    str_lst = val.split("-")
    val_int = [int(v) for v in str_lst]
    low,high = val_int
    age_avg = []
    age_avg = [int(a) for a in age_covid if len(a)==1 or len(a)==2 if int(a)>=low and int(a)<=high]
    summ = 0
    for aa in age_avg:
      summ+=aa
    new_age.append(str(round(summ/len(age_avg))))
  else:
    new_age.append(val)

new_age

#Q2
case1 = dictt_covid['date_onset_symptoms']
case2 = dictt_covid['date_admission_hospital']
case3 = dictt_covid['date_confirmation']

new_date_onset_symptoms = []
for datee in case1:
  temp = datee.split(".")
  dd,mm,yy = temp
  new_date_onset_symptoms.append(mm+'.'+dd+'.'+yy)
new_date_onset_symptoms

new_date_admission_hospital = []
for datee in case2:
  temp = datee.split(".")
  dd,mm,yy = temp
  new_date_admission_hospital .append(mm+'.'+dd+'.'+yy)
new_date_admission_hospital

new_date_confirmation = []
for datee in case3:
  temp = datee.split(".")
  dd,mm,yy = temp
  new_date_confirmation.append(mm+'.'+dd+'.'+yy)
new_date_confirmation

#Q3

latitude = dictt_covid['latitude']
longitude = dictt_covid['longitude']

#latitude = list(map(float,latitude))

latitude_enum = list(enumerate(latitude))

longitude_enum = list(enumerate(longitude))

from operator import itemgetter
idx = itemgetter(0)
search = itemgetter(1)

province = dictt_covid['province']

province_enum = list(enumerate(province))

latitude_new = []

import math

new_latitude = []
for lat in latitude_enum:

  if search(lat) == "NaN":
    
    index = idx(lat)
    key_prov = province[index]
    #print("key is ",key_prov)
    idx_prov = []
    for val in province_enum:
      if search(val) == key_prov:
        idx_prov.append(idx(val))
    #print("index_for NAN",i+1,idx_prov)
    temp = [float(latitude[indexx]) for indexx in idx_prov if latitude[indexx] != 'NaN']
    #find avg of temp
    summ = 0
    for t in temp:
      summ+=t
    avg = summ/len(temp)

    lat_nan = round(avg ,2)
    new_latitude.append(lat_nan)
  else:
    new_latitude.append(search(lat))
    
print(new_latitude)

new_longitude = []
for lon in longitude_enum:

  if search(lon) == "NaN":
    
    index = idx(lon)
    key_prov = province[index]
    #print("key is ",key_prov)
    idx_prov = []
    for val in province_enum:
      if search(val) == key_prov:
        idx_prov.append(idx(val))
    #print("index_for NAN",i+1,idx_prov)
    temp1 = [float(longitude[indexx]) for indexx in idx_prov if longitude[indexx] != 'NaN']
    #find avg of temp
    summ1 = 0
    for t in temp1:
      summ1+=t
    avg1 = summ1/len(temp1)

    lon_nan = round(avg1 ,2)
    new_longitude.append(lon_nan)
  
  else:
    new_longitude.append(search(lon))
    
print(new_longitude)

#Q4

city = dictt_covid['city']
city_enum = list(enumerate(city))

from collections import OrderedDict

update_city  = []
for c in city_enum:
  if search(c) == "NaN":
    index = idx(c)
    key_province = province[index]
    prov_idx = []
    filter_city = []
    for prov in province_enum:
      if  search(prov) == key_province:
        prov_idx.append(idx(prov))
    filter_city = [city[id] for id in prov_idx if city[id] != 'NaN']
    key_city = list(set(filter_city))
    value_city = [filter_city.count(k) for k in key_city]
    dictt_city = dict(zip(key_city,value_city))
    sorted_dict = dict(OrderedDict(sorted(dictt_city.items())))
    val = list(sorted_dict.keys())[0]
    update_city.append(val)
  else:
    update_city.append(search(c))

update_city

#Q5

symptoms_covid = dictt_covid['symptoms']
symptoms_enum = list(enumerate(symptoms_covid))

update_symtm = []
for sym in symptoms_enum:
  if search(sym) == 'NaN':
    idx_sym = idx(sym)
    nan_symptm = province[idx_sym]
    prov_idx = []
    filter_symptm = []
    for prov in province_enum:
      if  search(prov) == nan_symptm:
        prov_idx.append(idx(prov))
    filter_symptm = [symptoms_covid[id] for id in prov_idx if symptoms_covid[id] != 'NaN']
    final_list_symtm = []
    for temp in filter_symptm:
      l = temp.split(";")
      final_list_symtm = final_list_symtm+l
    key_symptm = list(set(final_list_symtm))
    value_symptm = [final_list_symtm.count(k) for k in key_symptm]
    dictt_fill_symptm = dict(zip(key_symptm,value_symptm))
    sorted_dict_symptm = dict(OrderedDict(sorted(dictt_fill_symptm.items())))
    val = list(sorted_dict_symptm.keys())[0]
    update_symtm.append(val)
  else:
    update_symtm.append(search(sym))

update_symtm

covid_id = dictt_covid['ID']

covid_age = dictt_covid['age']

covid_sex = dictt_covid['sex']

country = dictt_covid['country']

covid_data_new = []
for i in range(len(covid_id)):
  covid_data_new.append([covid_id[i],new_age[i],covid_sex[i],update_city[i],province[i],country[i],
                new_latitude[i],new_longitude[i],new_date_onset_symptoms[i],new_date_admission_hospital[i],
                new_date_confirmation[i],update_symtm[i]])

with open('/content/drive/MyDrive/ColabNotebooks/covidResult.csv','w',encoding='UTF8',newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(covid_data_new)
f.close()