import pandas as pd

chicago = pd.read_csv("chicago.csv")
chicago.head()
chicago.info()
chicago["Department"].nunique()
chicago["Department"].count()
chicago["Department"] = chicago["Department"].astype("category")
chicago["Department"].replace("OFFICER","STUFF")
chicago["Department"] = chicago["Department"].str.startswith("WATER")

chicago = chicago["Department"].str.lower()
chicago = chicago["Department"].str.upper()
chicago = chicago["Department"].str.Title()
len(chicago["Department"])
