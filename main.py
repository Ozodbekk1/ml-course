import opendatasets as od
import pandas as pd

od.download("https://www.kaggle.com/competitions/titanic/data")

df2 = pd.read_csv("/home/jasurbek/Desktop/ml-projects/titanic/train.csv")
df2.drop("Cabin", axis=1, inplace=True)
print(df2)