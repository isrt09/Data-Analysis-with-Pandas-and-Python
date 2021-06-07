import pandas as pd

week1     = pd.read_csv("Restaurant - Week 1 Sales.csv")
week2     = pd.read_csv("Restaurant - Week 1 Sales.csv")
customers = pd.read_csv("Restaurant - Customers.csv")
food      = pd.read_csv("Restaurant - Foods.csv")

len(week1)
len(week2)
len(pd.concat([week1,week2]))
pd.concat([week1,week2], ignore_index=True)