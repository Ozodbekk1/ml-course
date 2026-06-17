import opendatasets as od
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


od.download("https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques")

df = pd.read_csv("./house-prices-advanced-regression-techniques/train.csv")

somedata = df.isnull().sum().sort_values(ascending=False).head(15)
# print(somedata)

miss = (df.isnull().sum() / len(df) * 100).round(4)
miss40 = miss[miss>40].sort_values(ascending=False).head(15)
# print(miss)
# print(miss40)


sns.heatmap(df.isnull(), cbar=False, cmap="Reds")

# plt.show()

a =  ["PoolQC", "MiscFeature", "Alley", "Fence", "MasVnrType", "FireplaceQu"]

df.drop(a, axis=1, inplace=True)
print(df.isnull().sum().sort_values(ascending=False).head(15))


cat_all = df.select_dtypes(include="object").columns
df[cat_all] = df[cat_all].fillna("None")

print(df[cat_all])

num = df.select_dtypes(include="number").columns
df[num] = df[num].fillna(df[num].median())
print(df.isnull().sum().sum())

print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

print(df.dtypes.value_counts())


# df["MSSUBClass"] = df["MSSUBClass"].astype(str)
# print("Date" in df.columns)

Q1 = df["SalePrice"].quantile(0.25)
print(Q1)

Q3 = df["SalePrice"].quantile(0.75)
print(Q3)
IQR = Q3 - Q1

mask = (df["SalePrice"] >= Q1 - 1.5 * IQR) & (df["SalePrice"] <= Q3 + 1.5 * IQR)
print(mask)
df_clean = df[mask]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.stripplot(data=df, y="SalePrice", ax=axes[0])
axes[0].set_title("outline bor")

sns.stripplot(data=df_clean, y="SalePrice", ax=axes[1])
axes[1].set_title("outline olib tashlangan")

plt.tight_layout()
plt.show()

df_clean.to_csv("df_clean.csv", index=False)

# ffill()
# bfill()
# fillna(mode()[0])