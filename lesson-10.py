import numpy as np
import  pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

darmod = [1_000_000, 1_200_000, 110000, 1150000]

print(np.mean(darmod))

s = pd.Series(darmod)
print(s.mean())

print(s)


df = pd.DataFrame({"daromad": darmod})
print(df["daromad"].mean())

print(df)

data = [7, 9, 15, 21]
print(np.median(data))

print("ortacha", np.mean(darmod))
print("median", np.median(darmod))


df = pd.DataFrame({"daromad": darmod})
print("data frame bilan mean", df["daromad"].mean())


baholar = [5, 5, 3, 4, 4, 5, 3, 4, 5, 4, 2]

mode_result = stats.mode(baholar)
print(mode_result)
print(f"eng kop takrorlangan son {mode_result.mode}")
print(f"{mode_result.mode}, {mode_result.count} marta takrorlangan")


data = [2, 4, 4, 4, 5, 5, 7, 9]
print(np.var(data))

print(np.var(data, ddof=1))

s = pd.Series(data)
print(s.var())
print(s.var(ddof=0))

print(np.std(data))
print(np.std(data, ddof=1))


data = np.random.normal(170, 10, 1000)

mean = np.mean(data)
std = np.std(data)

plt.figure(figsize=(12, 6))

plt.hist(data, bins=30, color="#2ECB9B", alpha=0.7, edgecolor="white")

plt.title("talabalar boyi taqsimoti")
plt.xlabel("boyi sm")
plt.legend()
plt.tight_layout()
plt.show()



df = sns.load_dataset("penguins").dropna()

col = df["bill_length_mm"]

print("mean", col.mean())
print("median", col.median())
print("std", col.std())
print("var", col.var())

plt.figure(figsize=(12, 6))

plt.hist(col, bins=30, color="#2ECB9B", alpha=0.7, edgecolor="white")

plt.title("pingivinlar boyi (sm)")
plt.xlabel("boyi sm")
plt.legend()
plt.tight_layout()
plt.show()