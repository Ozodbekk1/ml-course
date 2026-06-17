import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import opendatasets as od

od.download(
    "https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset/data"
)

df = pd.read_csv("./car-price-prediction-dataset/cardekho.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df["selling_price"], kde=True)
plt.title("Selling Price Before Cleaning")

plt.subplot(1, 2, 2)
sns.boxplot(x=df["selling_price"])
plt.title("Selling Price Outliers")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values")
plt.show()

clean_df = df.copy()

clean_df = clean_df.drop_duplicates()

numeric_columns = clean_df.select_dtypes(include="number").columns

for column in numeric_columns:
    clean_df[column] = clean_df[column].fillna(
        clean_df[column].median()
    )

categorical_columns = clean_df.select_dtypes(include="object").columns

for column in categorical_columns:
    clean_df[column] = clean_df[column].fillna(
        clean_df[column].mode()[0]
    )

q1 = clean_df["selling_price"].quantile(0.25)
q3 = clean_df["selling_price"].quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

clean_df = clean_df[
    (clean_df["selling_price"] >= lower)
    & (clean_df["selling_price"] <= upper)
]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(clean_df["selling_price"], kde=True)
plt.title("Selling Price After Cleaning")

plt.subplot(1, 2, 2)
sns.boxplot(x=clean_df["selling_price"])
plt.title("Selling Price After Cleaning")

plt.tight_layout()
plt.show()

numeric_df = clean_df.select_dtypes(include="number")

plt.figure(figsize=(10, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

clean_df = pd.get_dummies(
    clean_df,
    drop_first=True
)

print(clean_df.shape)
print(clean_df.head())

# clean_df.to_csv(
#     "cleaned_car_price_dataset.csv",
#     index=False
# )

