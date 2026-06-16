import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")


def task_1():
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="muted"
    )

    df = sns.load_dataset("penguins")

    print(df.head())
    print("\n" + "=" * 50 + "\n")
    print(df.info())

    return df



def task_2(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="bill_length_mm",
        bins=30,
        kde=True
    )

    plt.title("Tumshug' uzunligi taqsimoti")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Count")

    plt.show()


def task_3(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="bill_length_mm",
        hue="species",
        bins=30,
        kde=True
    )

    plt.title("Tumshug' uzunligi taqsimoti (Species)")
    plt.show()

    print(
        "Izoh: Gentoo va Chinstrap penguinlarining "
        "tumshug'i Adelie turiga qaraganda uzunroq."
    )


def task_4(df):
    plt.figure(figsize=(8, 5))

    sns.kdeplot(
        data=df,
        x="body_mass_g",
        hue="species",
        fill=True,
        alpha=0.4
    )

    plt.title("Body Mass KDE by Species")
    plt.show()

    print(
        "Izoh: Taqsimotlar sezilarli darajada farq qiladi. "
        "Gentoo eng og'ir, Adelie esa eng yengil guruh hisoblanadi."
    )


def task_5(df):
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="species",
        y="flipper_length_mm",
        hue="sex"
    )

    plt.title("Flipper Length by Species and Sex")
    plt.show()

    print(
        "Izoh: Grafikdan ko'rinishicha Gentoo turida "
        "IQR nisbatan kattaroq."
    )


def task_6(df):
    plt.figure(figsize=(8, 5))

    sns.violinplot(
        data=df,
        x="species",
        y="bill_depth_mm",
        hue="sex",
        inner="box"
    )

    plt.title("Bill Depth by Species and Sex")
    plt.show()

    print(
        "Izoh: Violinplot boxplotdan tashqari "
        "taqsimot zichligi va shaklini ham ko'rsatadi."
    )


def task_7(df):
    plt.figure(figsize=(10, 5))

    sns.stripplot(
        data=df,
        x="island",
        y="body_mass_g",
        hue="species",
        jitter=True,
        alpha=0.6
    )

    plt.title("Body Mass by Island")
    plt.show()

    print(
        "Izoh: Eng og'ir penguinlar asosan Biscoe "
        "orolida uchraydi."
    )


def task_8(df):
    plt.figure(figsize=(8, 5))

    sns.regplot(
        data=df,
        x="bill_length_mm",
        y="bill_depth_mm",
        ci=95
    )

    plt.title("Bill Length vs Bill Depth")
    plt.show()

    print(
        "Izoh: Tumshuq uzunligi va chuqurligi o'rtasida "
        "ma'lum darajadagi bog'liqlik mavjud, ammo kuchli emas."
    )



def task_9(df):
    sns.jointplot(
        data=df,
        x="flipper_length_mm",
        y="body_mass_g",
        hue="species",
        kind="reg",
        height=8
    )

    plt.show()

    print(
        "Xulosa: Qanotlari uzunroq penguinlar "
        "odatda og'irroq bo'ladi."
    )



def task_10(df):
    fig, axes = plt.subplots(
        1,
        3,
        figsize=(15, 5)
    )

    sns.boxplot(
        data=df,
        x="species",
        y="body_mass_g",
        ax=axes[0]
    )
    axes[0].set_title("Body Mass")

    sns.violinplot(
        data=df,
        x="species",
        y="flipper_length_mm",
        ax=axes[1]
    )
    axes[1].set_title("Flipper Length")

    sns.stripplot(
        data=df,
        x="species",
        y="bill_length_mm",
        ax=axes[2]
    )
    axes[2].set_title("Bill Length")

    plt.tight_layout()
    plt.show()


task_7(df)