import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme()

def task1 ():
    plt.figure(figsize=(12, 6), dpi=120, facecolor="#315f87")

    x = [10, 20, 30, 40, 50]
    y = [5, 15, 10, 25, 20]

    plt.plot(
        x,
        y,
        color="blue",
        marker="o",
        linewidth=2
    )

    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.title("line graph")

    plt.grid(True)
    plt.show()

# task1()



def task2():
    students = ["Ali", "Vali", "Sardor", "Kamola", "Zulfiya"]
    scores = [88, 72, 95, 60, 81]

    colors = ["skyblue"] * len(scores)
    colors[scores.index(max(scores))] = "red"

    plt.figure(figsize=(8, 5))

    plt.bar(students, scores, color=colors)

    plt.title("O'quvchilar Baholari")
    plt.xlabel("O'quvchilar")
    plt.ylabel("Ball")

    plt.show()



# task2()



def task3():
    languages = ["Python", "JavaScript", "Java", "C++", "R"]
    popularity = [90, 85, 70, 65, 40]

    colors = ["blue", "gold", "green", "red", "purple"]

    plt.figure(figsize=(8, 5))

    plt.barh(languages, popularity, color=colors)

    plt.title("Dasturlash Tillari Mashhurligi")
    plt.xlabel("Mashhurlik")
    plt.ylabel("Til")

    plt.show()


# task3()


def task4():
    x = np.random.rand(100)
    y = np.random.rand(100)

    plt.figure(figsize=(8, 5))

    plt.scatter(
        x,
        y,
        color="green",
        alpha=0.5
    )

    plt.title("Tasodifiy nuqtalar")

    plt.show()


# task4()


def task5():
    heights = np.random.normal(
        loc=170,
        scale=10,
        size=300
    )

    plt.figure(figsize=(8, 5))

    plt.hist(
        heights,
        bins=25,
        edgecolor="white"
    )

    plt.xlabel("Bo'y (sm)")
    plt.ylabel("Soni")
    plt.title("Bo'y taqsimoti")

    plt.show()


# task5()


def task6():
    labels = [
        "Sport",
        "Musiqa",
        "Kitob",
        "Gaming",
        "Boshqa"
    ]

    sizes = [30, 25, 20, 15, 10]

    explode = [0.1, 0, 0, 0, 0]

    plt.figure(figsize=(8, 8))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        explode=explode,
        startangle=90
    )

    plt.title("Sinf Qiziqishlari")

    plt.show()


# task6()


def task7():
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot([1, 2, 3, 4], [2, 5, 3, 8])
    axs[0, 0].set_title("Line Plot")

    axs[0, 1].bar(
        ["A", "B", "C"],
        [5, 7, 3]
    )
    axs[0, 1].set_title("Bar Chart")

    x = np.random.rand(50)
    y = np.random.rand(50)

    axs[1, 0].scatter(x, y)
    axs[1, 0].set_title("Scatter Plot")

    data = np.random.normal(0, 1, 500)

    axs[1, 1].hist(data, bins=10)
    axs[1, 1].set_title("Histogram")

    plt.tight_layout()

    plt.show()


task7()




def task8():
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 13, 20, 18]

    plt.figure(figsize=(10, 5))

    plt.plot(
        x,
        y,
        color="blue",
        linestyle="--",
        marker="o",
        label="Natijalar"
    )

    plt.title("Bezatilgan Grafik")
    plt.xlabel("X qiymatlar")
    plt.ylabel("Y qiymatlar")

    plt.grid(True)
    plt.legend()

    plt.show()



# task8()



def task9():
    subjects = [
        "Math",
        "Physics",
        "English",
        "History",
        "IT"
    ]

    ali = [85, 90, 80, 75, 95]
    vali = [78, 85, 88, 82, 80]
    sardor = [92, 88, 91, 87, 97]

    plt.figure(figsize=(10, 5))

    plt.plot(
        subjects,
        ali,
        marker="o",
        color="blue",
        label="Ali"
    )

    plt.plot(
        subjects,
        vali,
        marker="s",
        color="green",
        label="Vali"
    )

    plt.plot(
        subjects,
        sardor,
        marker="^",
        color="red",
        label="Sardor"
    )

    plt.title("Fanlar bo'yicha baholar")
    plt.xlabel("Fanlar")
    plt.ylabel("Ball")

    plt.legend()
    plt.grid(True)

    plt.show()


# task9()



