import pandas as pd 
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

dict_table = {}
list_human = []
list_robot = []
list_names = []

for i in range(0, data.shape[0]):
    list_names.append(data.iloc[i, 0])

for i in list_names:
  if i == 'human':
    list_human.append(1)
    list_robot.append(0)
  else:
    list_human.append(0)
    list_robot.append(1)

dict_table['human'] = list_human
dict_table['robot'] = list_robot


df = pd.DataFrame(dict_table)
print(df)