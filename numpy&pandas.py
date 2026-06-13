import pandas as pd
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)

# ndarray = N-dimensional array

print(arr.shape)

print(arr.dtype)

# Number of elements.
print(arr.size)

# Number of Dimensions
print(arr.ndim)

# Creating Arrays Quickly
np.array([0,0,0,0,0])
print(np.zeros(45))
print(np.ones(12))
print(np.full(8, 10))

# Creating Sequences
print(np.arange(1, 20))
print(np.arange(0, 10, 2))

# linspace()
print(np.linspace(0, 10, 5)) # Give me 5 equally spaced points between 0 and 10

# Vectorization
arr = np.array([1,2,3,4])
print(arr * 2)



# solve problems
print("--------///////////------/////---//-/-////----/////")

print(np.arange(5, 26, 5))
print(np.zeros(10))
print(np.full(5, 7))
print(np.linspace(0, 100, 6))






data = {
    "ism": ["ozodbek", "oziy", "bbur"],
    "yosh": [25, 30, 35],
    "shahar": ["toshkent", "andijon", "toshkent viloyati"]
}

df = pd.DataFrame(data)

print(df.head(2))

print(df.columns)

print(df.dtypes)

print(df.describe())

print(df.shape)


data = {
    "product": ["laptop", "mishka", "kv", "display"],
    "narx": [1200, 25, 75, 300],
    "qolgan": [10, 100, 50, 20]
}

df = pd.DataFrame(data)

print(df[df["narx"] > 100])

print(df[df["qolgan"] < 30])

print(df[df["narx"].between(50, 500)])



df = pd.DataFrame(data)

df["inventory_value"] = df["narx"] * df["qolgan"]

df["expensive"] = df["narx"] > 100

print(df)


data = {
    "department": ["it", "HR", "swe", "finance", "HR", "finance"],
    "salary": [5000, 3500, 6000, 7000, 4000, 8000]
}

df = pd.DataFrame(data)

avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)

max_salary = df.groupby("department")["salary"].max()
print(max_salary)

employee_count = df.groupby("department")["salary"].count()
print(employee_count)



data = {
    "ism": ["ozodbek", "oziy", None, "bob"],
    "yosh": [25, None, 30, 40],
    "salary": [50000, 60000, None, 70000]
}

df = pd.DataFrame(data)

print(df.isna().sum())

clean_df = df.dropna()
print(clean_df)

df["yosh"] = df["yosh"].fillna(df["yosh"].mean())

df["ism"] = df["ism"].fillna("Unknown")

print(df)