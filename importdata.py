import pandas as pd 

#Read csv
df = pd.read_csv('Data/applicants250.csv',na_values=['a','b'])

#create overview of columns
df.columns

#initialise tag column
tags = ''
df['tag'] = tags

#write csv 
df.to_csv('Data/applicants250.csv')



