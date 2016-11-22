'''
Step 1 - basic operations, setting up
documentation: http://pandas.pydata.org/pandas-docs/stable/
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
A Series is a one-dimensional object similar to an array, list, or column in a table.
It will assign a labeled index to each item in the Series.
By default, each item will receive an index label from 0 to N, where N is the length of the Series minus one.
'''
s = pd.Series([7, 'Test', 8])

p = pd.Series([1, 2, "H"],
              index=["A","B","C"])

#The Series constructor can convert a dictonary as well, using the keys of the dictionary as its index.

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}

cities = pd.Series(d)

print(cities['Chicago'])
print(cities[['Chicago', 'Portland', 'San Francisco']])

print(cities[cities < 1000])
print(cities < 1000)
cities[cities < 1000] = 750
print(cities)

print('Chicago' in cities)
#print(cities / 3)

cummulative = cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']]
print("cummulative", cummulative[cummulative.notnull()])
print(cities[cities.isnull()])

'''
A DataFrame is a tablular data structure comprised of rows and columns, akin to a spreadsheet, database table, or R's data.frame object.
You can also think of a DataFrame as a group of Series objects that share an index (the column names).
'''

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

football = pd.DataFrame(data)
football2 = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses']) #if you want to specify columns manually

from_csv = pd.read_csv('baseball.csv')
print(from_csv.head(5))
print(from_csv.head(3)['Age'])

#cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
#        'result', 'quarter', 'distance', 'receiver', 'score_before',
#        'score_after']
#no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,
#                         names=cols)

'''
#Read from SQL
import sqlite3

conn = sqlite3.connect('/Users/gjreda/Dropbox/gregreda.com/_code/towed')
query = "SELECT * FROM towed WHERE make = 'FORD';"

results = sql.read_sql(query, con=conn)
results.head()

#Read from clipboard
hank = pd.read_clipboard()

#Read from URL
url = 'https://raw.github.com/gjreda/best-sandwiches/master/data/best-sandwiches-geocode.tsv'
from_url = pd.read_table(url, sep='\t')
'''

