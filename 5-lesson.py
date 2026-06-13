import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import title

sns.set_theme(rc={"figure.figsize": (10, 6)})

tips = sns.load_dataset("tips")

# sns.histplot(data=tips, x="total_bill",  bins=30)
#
# tips.describe()

# for contex in ["paper", "notebook", "talk", "poster"]:
#     sns.set_theme(context=contex)
#     sns.histplot(data=tips, x="total_bill")
#     plt.title(f"context: {contex}")
#     plt.show()

# with sns.axes_style("white"):
#     sns.histplot(data=tips)


# sns.set_style("whitegrid", {
#     "grid.linesttyle": ":",
#     "grid.linewidth": 2,
#     "axes.spines.top": False,
#     "axes.spines.right": False
#
# })

# plt.figure(figsize=(10, 6))
# sns.scatterplot(
#     data=tips,
#     x="total_bill",
#     y="tip",
#     style="smoker"
# )

# sns.kdeplot(data=tips, x="total_bill")

# sns.kdeplot(
#     data=tips,
#     x="total_bill",
#     hue="sex",
#     fill=True,
#     alpha=0.5
# )

# sns.boxplot(
#     data=tips,
#     x="day",
#     y="total_bill",
#     hue="sex",
#     width=1,
#     gap=0.2
# )

# plt.legend(
#     title("salom"),
#     fontsize=8,
#     title_fontsize=10,
#     markerscale=10,
#     loc="upper right"
# )

# plt.figure(figsize=(10, 6))
# sns.violinplot(
#     data=tips,
#
# )

# sns.stripplot(
#     data=tips,
#     x="day",
#     y="total_bill",
#     jitter=True,
#     alpha=0.5,
#     marker="o",
#     s=5,
#     color="red"
# )

# sns.regplot(data=tips, x="total_bill", y="tip")

# sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
#
# sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde")
#
# sns.jointplot(data=tips, x="total_bill", y="tip", kind="hist")
#
# sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg")


# Load the example flights dataset and convert to long-form
# flights_long = sns.load_dataset("flights")
# flights = (
#     flights_long
#     .pivot(index="month", columns="year", values="passengers")
# )
#
# # Draw a heatmap with the numeric values in each cell
# f, ax = plt.subplots(figsize=(9, 6))
# sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()


# matplotlib = legend, seaborn = hue
#  loc = location of legend