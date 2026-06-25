import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_theme()

df = pd.read_csv("./df_clean_HOUSE_PRICE.csv")

print(df)

print(df.describe())

print(df.info())

print(df.dtypes.value_counts())

print(df.isnull().sum().sum())

cat_all = df.select_dtypes(include="object").columns
df[cat_all] = df[cat_all].fillna("None")

nums = df.select_dtypes(include="number").columns
df[nums] = df[nums].fillna(df[nums].median())

print(df.isnull().sum().sum())

# sns.histplot(df["SalePrice"], kde=True, color="red")

# sns.boxplot(df["SalePrice"])

# fig, axes = plt.subplots(1, 3, figsize=(15,5))
#
# # 1. Histogram
# sns.histplot(df['SalePrice'], ax=axes[0], color='#2ECB9B', kde=True, bins=10)
# axes[0].set_title('Taqsimot')
# axes[0].tick_params(axis='x', rotation=45)
#
#
# # 2. KDE
# sns.kdeplot(df['SalePrice'], ax=axes[1], fill=True, color='#2ECB9B', bw_adjust=0.2)
# axes[1].set_title('KDE egri chizig\'i')
# axes[1].tick_params(axis='x', rotation=45)
#
#
# # 3. Boxplot
# sns.boxplot(y=df['SalePrice'], ax=axes[2], color='#2ECB9B')
# axes[2].set_title('Boxplot — outlier')
#
# plt.tight_layout()
# plt.show()

#
# df["SalePrice_log"] = np.log1p(df["SalePrice"])
#
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
#
# sns.histplot(df["SalePrice"], ax=axes[0], color="#EF4444", kde=True)
#
# axes[0].set_title("asl ")
#
# sns.histplot(df["SalePrice_log"], ax=axes[1], color="#2ECB9B", kde=True)
#
# axes[1].set_title("log normal")
#
# plt.tight_layout()
#
# plt.show()

# Ragamli ustunlar

# num_df = df.select_dtypes (include='number')
# corr = num_df.corr()
#
# print(corr['SalePrice'].drop('SalePrice'))
#
#  # Top 10 SalePrice bilan
# top10 = corr['SalePrice'].drop('SalePrice').abs().sort_values(ascending=False).head(20).index
# top_cols = list(top10) + ['SalePrice']
#
#  # print(top10) 12
#  # Heatmap I 14
# plt.figure(figsize=(11, 8))
#
# sns.heatmap(corr[top_cols].loc[top_cols], annot=True, fmt='.2f', center=0, vmin=-1, vmax=1, cmap="magma" )
# plt.title('Top 10 Korrelyatsiya')
# plt.show()


fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=df, x="OverallQual", y="SalePrice", palette="magma", ax=axes[0])
axes[0].set_title("sifat va narx box plot")

sns.violinplot(data=df, x="OverallQual", y="SalePrice", palette="magma", ax=axes[1])
axes[1].set_title("sifat va narx violin")

plt.tight_layout()
plt.show()

