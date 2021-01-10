# pandas is a library for data manipulation and analysis

'''
# import pandas as pd
import pandas as pd

pd.Series

animals = ['Lion', 'Tiger', 'Jaguar']
pd.Series(animals)
print(pd.Series(animals))

# Querying a series
sports = {'France': 'Football',
          'USA': 'Basketball',
          'India': 'Hockey',
          'China': 'Badminton'}

s = pd.Series(sports)
print(s)

# loc and iloc are attributes not methods
print(s.iloc[3])  # this attribute will lock the 3rd value in the sports series
print(s.loc['Hockey'])


# creation of data frames in python using the pandas library
import pandas as pd

# data frame data structures
player_1 = pd.Series({"Name": "Messi",
                      "Position": "Forward",
                      "Role": "Captain"})
player_2 = pd.Series({"Name": "Neymar",
                      "Position": "Left Winger",
                      "Role": "Attacker"})
player_3 = pd.Series({"Name": "Pique",
                      "Position": "Defender",
                      "Role": "Vice Captain"})
player_4 = pd.Series({"Name": "Sergio",
                      "Position": "Midfielder",
                      "Role": "Defensive Mid"})
df = pd.DataFrame([player_1, player_2, player_3, player_4], index = ['Attacker', 'Attacker', 'Defender', 'Midfilder'])
df.head()
print(df.head())


# An another record
# sales record

import pandas as pd

purchase_1 = pd.Series({'Shop': 'Cothes',
                        'item_buy': 'Shirt',
                        'Price': 2500})
purchase_2 = pd.Series({'Shop': 'Toys',
                        'item_buy': 'Car',
                        'Price': 25})
purchase_3 = pd.Series({'Shop': 'Books',
                        'item_buy': 'book',
                        'Price': 250})
purchase_4 = pd.Series({'Shop': 'Cothes',
                        'item_buy': 'Jeans',
                        'Price': 25000})
purchase_5 = pd.Series({'Shop': 'Books',
                        'item_buy': 'Novel',
                        'Price': 350})
purchase_6 = pd.Series({'Shop': 'Cothes',
                        'item_buy': 'Trousers',
                        'Price': 1500})
purchase_7 = pd.Series({'Shop': 'Colors',
                        'item_buy': 'Paint',
                        'Price': 4570})
purchase_8 = pd.Series({'Shop': 'Stationary',
                        'item_buy': 'Pens',
                        'Price': 25})
purchase_9 = pd.Series({'Shop': 'Cothes',
                        'item_buy': 'Jacket',
                        'Price': 5000})
df = pd.DataFrame(
    [purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6, purchase_7, purchase_8, purchase_9],
    index=['Clothes_Shop', 'Toy_Shop', 'Book_Shop', 'Clothes_Shop', 'Book_Shop', 'Clothes_Shop', 'Color_Shop',
           'Stationary_Shop', 'Clothes_Shop'])

print(df)
# drop function
# it uses to drop the coloumns or th variables from the data frame
print(df.drop('Book_Shop'))

# a data frame has been created

# Data frame indexing and loading
price  = df['Price']
print(price)

price += 100000  # how to alter the data
print(price)

'''
'''
import pandas as pd
import csv

File = 'Customer.csv'
df = pd.read_csv('Customer.csv')
print(df)

# boolean masking
# or to apply the boolean or conditions to sort out or clean the data

only_region = df.where(df('Region' = 'South'))
print(only_region)
'''
# indexing the dataframes


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print(df)

# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])

# providing an index
ser = pd.Series(data, index=[10, 11, 12, 13, 14])
print(ser) 