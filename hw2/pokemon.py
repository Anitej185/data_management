# -*- coding: utf-8 -*-
"""pokemon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YgCGDPr97cWcCi9neOBT81XrC5LEfZOc
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

import csv
import math

from google.colab import drive
drive.mount('/content/drive/')

path_pokemon = '/content/drive/MyDrive/ColabNotebooks/pokemonTrain.csv'

file = open(path_pokemon)

type(file)

csvreader = csv.reader(file)

# extracting field names
header = []
header = next(csvreader)
#header

rows = []
for row in csvreader:
  rows.append(row)

dictt = {}
for c in range(len(header)):
  val = []
  for r in range(len(rows)):
    val.append(rows[r][c])
  dictt[header[c]] = val

#dictt

e = list(enumerate(header))

#Q.1 calculate index of fire pokemonn in key type
type_val = dictt['type']
#type_val

type_val_lst = list(enumerate(type_val))

from operator import itemgetter
idx = itemgetter(0)
search = itemgetter(1)
type_idx_fire = [idx(val) for val in type_val_lst if search(val) == 'fire']

# index where pokemonn type is fire
type_idx_fire

# list of level which is to be searched against the indexes greater yhan 40
levell = (dictt['level'])

# convert into int using map
levell = list(map(float,levell))

print(levell)

fire_level = [levell[i] for i in type_idx_fire if levell[i]>=40.0]

total_fire_level = [levell[i] for i in type_idx_fire]

fire_level = list(map(float,fire_level))
fire_level

sum_fire_level = len(fire_level) / len(total_fire_level)

sum_fire_level

percentage_fire_level = round(sum_fire_level*100)

path_Q1 = '/content/drive/MyDrive/ColabNotebooks/pokemon1.txt'

file1 = open(path_Q1,'w+')

file1.write('Percentage of fire type Pokemons at or above level 40 = '+str(percentage_fire_level)+'\n')
file1.close()

"""Question 2"""

from collections import defaultdict
from collections import Counter
list4 = list(zip(dictt['weakness'], dictt['type']))
dict1 = defaultdict(list)
for k, v in list4:
    if (v != 'NaN'):
        dict1[k].append(v)
for i in range(len(dictt['type'])):
    if (dictt['type'][i] == 'NaN'):
        j = dictt['weakness'][i]
        ctr = Counter(dict1[j])
        guess = max(ctr, key=ctr.get)
        dictt['type'][i] = guess
dictt

"""Question 3"""

#Q3

# filling atk, def, hp
level_below_40 = []
level_above_40 = []
for l in levell:
  if l>40.0:
    level_above_40.append(l)
  else:
    level_below_40.append(l)

import numpy as np
val_below_40 = round(np.array(level_below_40).mean(),1)
val_above_40 = round(np.array(level_above_40).mean(),1)

atk_lst = dictt['atk']
def_lst = dictt['def']
hp_lst = dictt['hp']

set(atk_lst)

atk_lst = list(map(float,atk_lst))
def_lst = list(map(float,def_lst))
hp_lst = list(map(float,hp_lst))

# creating new list for atk, def, hp
atk_new = []
def_new = []
hp_new = []

for i in range(len(atk_lst)):
  if math.isnan(atk_lst[i]) == True:
    if levell[i]>40.0:
      atk_new.append(str(val_above_40))
    else:
      atk_new.append(str(val_below_40))
  else:
    atk_new.append(atk_lst[i])

for i in range(len(def_lst)):
  if math.isnan(def_lst[i]) == True:
    #print("yes",i)
    if levell[i]>40.0:
      def_new.append(str(val_above_40))
    else:
      def_new.append(str(val_below_40))
  else:
    print(i)
    def_new.append(def_lst[i])

for i in range(len(hp_lst)):
  if math.isnan(hp_lst[i]) == True:
    if levell[i]>40.0:
      hp_new.append(str(val_above_40))
    else:
      hp_new.append(str(val_below_40))
  else:
    hp_new.append(hp_lst[i])

new_type = []
for i in range(len(type_val)):
   if type_val[i] == 'NaN':
     new_type.append(nan_replace)
   else:
    new_type.append(type_val[i])
#new_type

id_list = dictt['id']
name_list = dictt['name']
level_list = dictt['level']
personality_list = dictt['personality']
type_list = new_type
weakness_list = dictt['weakness']
atk_list = atk_new
def_list = def_new
hp_list = hp_new
stage_list = dictt['stage']

dataa = []
for i in range(len(id_list)):
  dataa.append([id_list[i],name_list[i],level_list[i],personality_list[i],type_list[i],weakness_list[i],
                atk_list[i],def_list[i],hp_list[i],stage_list[i]])

with open('/content/drive/MyDrive/ColabNotebooks/pokemonResult.csv','w',encoding='UTF8',newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(dataa)
f.close()

# to conquer question we first find the unique pokemon and find their indexes
# then we map those indexes to personalities 
# we then make dictionary with key as pokemon name and personalities as dict values
from collections import defaultdict
pokemon_personality = defaultdict(list)

path_pokemon_new = '/content/drive/MyDrive/ColabNotebooks/pokemonResult.csv'

file = open(path_pokemon_new)

csvreader = csv.reader(file)

# extracting field names
header = []
header = next(csvreader)
#header

rows = []
for row in csvreader:
  rows.append(row)

dictt_new = {}
for c in range(len(header)):
  val = []
  for r in range(len(rows)):
    val.append(rows[r][c])
  dictt_new[header[c]] = val

pokemon_lst = dictt_new['name']
pokemon_name = list(set(pokemon_lst))

pokemon_lst_enum = list(enumerate(pokemon_lst))

pokemon_personality_lst = dictt_new['personality']

from operator import itemgetter
idx = itemgetter(0)
search = itemgetter(1)
for i in pokemon_lst:
  list_idx_per = []
  for j in pokemon_lst_enum:
    if search(j) == i:
      list_idx_per.append(idx(j))
  per_name= []
  for per in list_idx_per:
    per_name.append(pokemon_personality_lst[per])
  pokemon_personality[i] = list(set(sorted(per_name)))

from collections import OrderedDict
 
pokemon_personality_dict = dict(OrderedDict(sorted(pokemon_personality.items())))
print(pokemon_personality_dict)

"""Question 4"""

#Q4 - Print the dictionary to a file named "pokemon4.txt"

pokemon_keys_list = list(pokemon_personality_dict.keys())
#pokemon_keys_list

with open('/content/drive/MyDrive/ColabNotebooks/pokemon4.txt', "w") as f:
  f.write("Pokemon type to Personality mapping :")
  for key in pokemon_keys_list:
    value_key = list(pokemon_personality_dict[key])
    str_val = ",".join(value_key)
    #print(str_val)
    f.writelines(key+":"+str_val+"\n")

hit_points_stage3 = [float(dictt_new['hp'][i]) for i in range(len(dictt_new['hp'])) if dictt_new['stage'][i] == '3.0']

sum = 0
for elem in hit_points_stage3:
  sum+= elem
sum / len(hit_points_stage3)
hitpoint_s3_avg = sum/len(hit_points_stage3)
print('Average hit point for Pokemons of stage 3.0 = {}'.format(hitpoint_s3_avg))

sum = 0
for elem in hit_points_stage3:
  sum+= elem
sum / len(hit_points_stage3)

"""Question 5"""

#Q5 - final txt file

path_Q5 = '/content/drive/MyDrive/ColabNotebooks/pokemon5.txt'

file2 = open(path_Q5,'w+')



file2.write('Average hit point for Pokemons of stage 3.0 = ' + str(hitpoint_s3_avg)+'\n')
file2.close()