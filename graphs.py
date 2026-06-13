import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns
from matplotlib import markers
from matplotlib.lines import lineStyles
from matplotlib.pyplot import axes

# %matplotlib inline

# plt.figure(figsize=(12, 6), dpi=120, facecolor="#315f87")
# sns.set_theme()
#
# plt.plot([1, 1, 9], [9, 2, 6])
# plt.show()
#
# fig, ax = plt.subplots()
#
# ax.plot([2021, 2022, 2023], [900, 200, 600])
#
# ax.set_title("My Graph")
#
# ax.set_xlabel("yil")
# ax.set_ylabel("sotuv")
# plt.show()

# fig, ax = plt.subplots()
#
# ax.plot([2021, 2022, 2023], [900, 200, 600])
#
# ax.set_xticks([2021, 2022, 2023])
#
# ax.set_title("My Graph")
# ax.set_xlabel("yil")
# ax.set_ylabel("sotuv")
#
# plt.show()
#

def graphs():


    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot([1, 2, 3], [4, 5, 6])
    axes[0].set_title("Birinchi")
    axes[0].set_xlabel("X")
    axes[0].set_ylabel("Y")
    axes[0].set_facecolor("#27F5B0")
    axes[0].grid(False)

    axes[1].plot([1, 2, 3], [6, 5, 4])
    axes[1].set_title("Ikkinchi")
    axes[1].set_xlabel("X")
    axes[1].set_ylabel("Y")
    axes[1].set_facecolor("#FFE175")
    axes[1].grid(True)

    plt.show()

# graphs()


def graph():
    years = [2020, 2021, 2022, 2023, 2024]

    laptop_sales = [500, 700, 900, 1200, 1400]
    phone_sales = [800, 950, 1100, 1300, 1600]
    tablet_sales = [300, 450, 400, 550, 700]
    watch_sales = [200, 300, 450, 600, 850]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(years, laptop_sales, label="Laptop", marker="o", linewidth=2, linestyle="--")
    ax.plot(years, phone_sales, label="Phone", marker="s", linewidth=2)
    ax.plot(years, tablet_sales, label="Tablet", marker="^", linewidth=2)
    ax.plot(years, watch_sales, label="Watch", marker="D", linewidth=2)

    ax.set_title("Mahsulotlar bo'yicha yillik sotuvlar")
    ax.set_xlabel("Yil")
    ax.set_ylabel("Sotuv")
    ax.set_xticks(years)

    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

# graph()

def graphh():
    shaharlar = ["toshkent", "samarqand", "buxoro", "namangan"]
    sotuv = [450, 280, 190, 320]
    fig, ax = plt.subplots()
    ax.barh(shaharlar, sotuv, color="#a15843", edgecolor="#a1225f", linewidth=3, height=0.5)

    ax.set_title("sotuvlar jarayoni")
    ax.set_xlabel("shaharlar boyicha sotuv")
    ax.set_ylabel("shahar")
    ax.grid(axis="y")
    plt.show()

# graphh()

def scattr():
    import numpy as np
    x = np.random.randint(40, 500, 80)
    y = 0.5 * x + np.random.normal(0, 30, 80)
    fig, ax= plt.subplots()
    ax.scatter(x, y, s=80, c="steelblue", alpha=0.5, marker="o"),
    ax.set_title("uy narxi vs narxi")
    ax.set_xlabel("maydon m kv")
    ax.set_ylabel("narx mln som")
    ax.grid(True)
    plt.show()

# scattr()

def pie_chart():
    fig, ax = plt.subplots()

    ulushlar=[40, 30, 20, 10]

    nomlar=["python", "ml", "ai", "sql"]

    colors=["red", "green", "blue", "yellow"]

    ax.pie(
        ulushlar,
        colors=colors,
        labels=nomlar,
        autopct="%1.1f%%",
        explode=[0, 0.1, 0, 0]
    )

    ax.set_title("kurs tolovi")
    plt.show()

# pie_chart()


def multi_subplots():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    x = np.random.randint(40, 500, 80)
    y = 0.5 * x + np.random.normal(0, 30, 80)

    axes[0].scatter(x, y, s=80, c="steelblue", alpha=0.5, marker="o")
    axes[0].set_title("Uy narxi vs maydon")
    axes[0].set_xlabel("Maydon (m²)")
    axes[0].set_ylabel("Narx (mln so'm)")
    axes[0].grid(True)

    ulushlar = [40, 30, 20, 10]
    nomlar = ["python", "ml", "ai", "sql"]
    colors = ["red", "green", "blue", "yellow"]

    axes[1].pie(
        ulushlar,
        colors=colors,
        labels=nomlar,
        autopct="%1.1f%%",
        explode=[0, 0.1, 0, 0]
    )

    axes[1].set_title("Kurs taqsimoti")

    plt.tight_layout()
    plt.show()

multi_subplots()