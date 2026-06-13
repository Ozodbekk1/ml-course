import opendatasets as od
import pandas as pd
import numpy as np

print(np.__version__)

od.download("https://www.kaggle.com/competitions/titanic/data")

df2 = pd.read_csv("./titanic/train.csv")
df2.drop("Cabin", axis=1, inplace=True)
print(df2)
print("your datas is:")
print(df2.head())
print(df2.tail())
