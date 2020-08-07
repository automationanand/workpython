
# Converting json date to pandas dataframe and saving into CSV formate
from pandas.io.json import json_normalize
import csv
import json
with open('example_2.json')as f:
    sam=json.load(f)
s=json_normalize(sam)
print(s.columns) # colunm list
print(s.loc[0,'quiz.sport.q1.options'])
s.to_csv('json_date_to_csv.csv')

#Command line arguments
import sys
print(sys.argv)

def addd(a,b):
   c=a+b
   return print(c)
addd(int(sys.argv[1]),int(sys.argv[2]))
# C:\Users\Dell\Desktop\PANDAS>python prac_delet.py 1 2
# ['prac_delet.py', '1', '2']
# 3