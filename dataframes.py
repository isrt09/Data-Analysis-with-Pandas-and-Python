import pandas as pd

data = pd.read_csv("jamesbond.csv")
data.set_index("Film", inplace=True)
data.reset_index(drop=False, inplace=True)


# Index by Label
data = pd.read_csv("jamesbond.csv", index_col="Film")
data.sort_index(inplace=True)
data.head()
data.loc["A View to a Kill"]
data.loc["GoldenEye"]
data.loc["Casino Royale"]
data.loc["Casino Royale" : "Moonraker"]
data.loc["CasinoRoyale " : ]
data.loc[["Casino Royale","Moonraker","Die Another Day"]]
"Casino Royale" in data.index

# Index by Position
data = pd.read_csv("jamesbond.csv")
data.sort_index(inplace=True)
data.head()
data.loc[10]
data.loc[[1,3,5,7]]

data.iloc[10]
data.iloc[[1,3,5,7]]
data.iloc[5:]
data.iloc[3:7]

data = pd.read_csv("jamesbond.csv",index_col="Film")
data.sort_index(inplace=True)
data.head()

data.iloc[10]
data.iloc[[1,3,5,7]]
data.iloc[5:]
data.iloc[3:7]