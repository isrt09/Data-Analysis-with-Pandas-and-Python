import pandas as pd

data = pd.read_csv("jamesbond.csv")
data.set_index("Film", inplace=True)
data.reset_index(drop=False, inplace=True)
