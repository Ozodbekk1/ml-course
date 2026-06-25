from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

sns.set_theme()

mu = 170
sigma = 10

x = np.linspace(130, 210, 300)
y = stats.norm.pdf(x, mu, sigma)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(x, y, color="#2ECB9B", linewidth=2.5)
axes[0].fill_between(x, y, alpha=0.3, color="#2ECB9B")
axes[0].axvline(mu, color="red", linestyle="--")
axes[0].set_title("normal pdf boy taqsimoti")

samples = np.random.normal(mu, sigma, 1000)
axes[1].hist(samples, bins=20, color="#2ECB9B", edgecolor="white")
# axes[1].fill_between(x, y, alpha=0.3, color="#2ECB9B")
axes[1].axvline(mu, color="red", linestyle="--")
axes[1].set_title("1000 ta tasodifiy namuma")

plt.tight_layout()
# plt.show()

n = 10
p = 0.5

k = np.arange(0, n+1)

pmf = stats.binom.pmf(k, 10, 0.5)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(k, pmf, color="#3B82F6", edgecolor="white")
axes[0].set_title("binomal pmf n =10 p=0.5")

pmf2 = stats.binom.pmf(k, n, 0.3)
axes[1].bar(k-0.2, pmf, width=0.4, label="p=0.5", color="#3B82F6")
axes[1].bar(k+0.2, pmf2, width=0.4, label="p=0.3", color="red")
axes[1].legend()
axes[1].set_title("p=0.5 vs p=0.3")
plt.tight_layout()
# plt.show()

lam = 3
k = np.arange(0, 15)

pmf = stats.poisson.pmf(k, 5)

fig, axes = plt.subplots(1, 5, figsize=(15, 4))

for ax, l in zip(axes, [1, 2, 3, 5, 8]):
    ax.bar(k, stats.poisson.pmf(k, l))
    ax.set_title(f"poission lambda {l}")
    ax.axvline(l, color="red", linestyle="--", label=f"lambda{l}")

plt.tight_layout()
plt.show()