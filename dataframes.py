import pandas as pd

data = pd.read_csv("jamesbond.csv")
data.set_index("Film", inplace=True)
data.reset_index(drop=False, inplace=True)


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