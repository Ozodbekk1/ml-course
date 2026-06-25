import opendatasets as od
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

od.download("https://www.kaggle.com/competitions/playground-series-s6e6")

df = pd.read_csv("./playground-series-s6e6/train.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())
print(df.duplicated().sum())

numeric_cols = df.select_dtypes(include=np.number).columns



plt.figure(figsize=(10, 5))
sns.histplot(df["redshift"], kde=True)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x=df["redshift"])
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df.sample(5000),
    x="u",
    y="g",
    hue="class"
)
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(
    data=df.sample(5000),
    x="r",
    y="i",
    hue="class"
)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(
    data=df,
    x="class",
    y="redshift"
)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(
    data=df,
    x="spectral_type",
    y="redshift"
)
plt.show()

corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, cmap="coolwarm", annot=True)
plt.show()

top_features = [
    "u",
    "g",
    "r",
    "i",
    "z",
    "redshift"
]

sns.pairplot(
    df[top_features].sample(2000)
)
plt.show()

Q1 = df["redshift"].quantile(0.25)
Q3 = df["redshift"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df[
    (df["redshift"] >= lower)
    & (df["redshift"] <= upper)
]

print(df_clean.shape)

