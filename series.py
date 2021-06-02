import pandas as pd

# Create Object from list, dictionary and boolean

ice_cream    = ['Vanilla','Chocolate','Straberry']
lottery      = [10,11,34,23,45,50]
registration = [True,False,True,False]
webster 	 = { "Tiger" : 'A Dangerous Animal',
            	 "Banana": 'Tastefull Fruits',
            	 "Cyan"  : 'A Beautiful Color'
               }

pd.Series(lottery)
pd.Series(registration)
pd.Series(ice_cream)
pd.Series(webster)

# Attribute & Methods

quality = ["Genius","Handsome","Cheater","Brilliant","Humble", "Smart"]
s = pd.Series(quality)
s
s.index
s.values
s.dtype

price = [2.56,3.24,4.45,8.3,5,5.5]
s = pd.Series(price)
s
s.sum()
s.mean()
s.min()
s.max()
s.var()
s.std()
s.count()
s.product()

# Parameters and Arguments

roll  = [1001,1002,1003,1004,1005]
grade = ["A+","B","A","C","B+"]
pd.Series(roll, grade)
pd.Series(data=grade, index=roll)
pd.Series(grade, index=roll)

# import data csv file
pd.read_csv('pokemon.csv')
pd.read_csv('pokemon.csv', usecols=['Pokemon'])
pd.read_csv('pokemon.csv', usecols=['Pokemon'], squeeze=True)
pd.read_csv('pokemon.csv', squeeze=True)

pokemon = pd.read_csv('pokemon.csv', usecols=['Pokemon'], squeeze=True)
pokemon.head()
pokemon.tail()


# Built-in Functions in Python
pd.read_csv('pokemon.csv')
pokemon
len(pokemon)
type(pokemon)
max(pokemon)
min(pokemon)
sorted(pokemon)
list(pokemon)
dict(pokemon)

# More Series Attributes
pokemon = pd.read_csv('pokemon.csv')
pokemon = pd.read_csv('pokemon.csv', usecols=['Pokemon'])
pokemon = pd.read_csv('pokemon.csv', usecols=['Pokemon'], squeeze=True)
pokemon.head()
pokemon.tail()
pokemon.name
pokemon.size
pokemon.shape
pokemon.ndim
pokemon.dtype
pokemon.index
pokemon.values
pokemon.is_unique
pokemon.sort_values()
pokemon.sort_values().head()
pokemon.sort_values().tail()
pokemon.sort_values(ascending=True)
pokemon.sort_values(ascending=False)
pokemon.sort_values(ascending=True, inplace=True)
pokemon.sort_values(ascending=True, inplace=False)
pokemon.sort_index(ascending=False)
pokemon.sort_index(ascending=True)
pokemon.sort_index(ascending=True, inplace=True)
pokemon.sort_index(ascending=True, inplace=False)

# In Keyword
pokemon = pd.read_csv('pokemon.csv')
pokemon = pd.read_csv('pokemon.csv', usecols=['Pokemon'])
pokemon = pd.read_csv('pokemon.csv', usecols=['Pokemon'], squeeze=True)

100 in [1,2,3,5]
100 in pokemon.index
'Charmeleon' in pokemon.values
'Mazedur' in pokemon.values