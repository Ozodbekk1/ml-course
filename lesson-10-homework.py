import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("./car-price-prediction-dataset/cardekho.csv")



df["Brand"] = df["name"].str.split().str[0]

df.drop("name", axis=1, inplace=True)



numeric_cols = [
    "mileage(km/ltr/kg)",
    "engine",
    "max_power",
    "seats"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())



categorical_cols = [
    "fuel",
    "seller_type",
    "transmission",
    "owner",
    "Brand"
]

df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)



target = "selling_price"

feature_cols = df.drop(columns=[target]).columns

numerical_features = df[feature_cols].select_dtypes(
    include=["int64", "float64", "bool"]
).columns

scaler = StandardScaler()

df[numerical_features] = scaler.fit_transform(
    df[numerical_features]
)

#
# df.to_csv(
#     "car_price_preprocessed.csv",
#     index=False
# )
#
# print(df.head())
# print(df.shape)
# print("completed")


print("info")
print(df.info())

print("check")
print(df.isna().sum().sort_values(ascending=False).head(10))

print("after scailing")
print(df.describe().round(3))