import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_csv('uylar_dataseti.csv')

X = df[['Kvadrat_Metr']]
y = df['Narxi_USD']

model = LinearRegression()
model.fit(X, y)

print("madel learned successfully")

try:
    user_kv = float(input("please insert house kvm: "))
    predicted_price = model.predict([[user_kv]])[0]

    yakin_uylar = df[(df['Kvadrat_Metr'] >= user_kv - 10) & (df['Kvadrat_Metr'] <= user_kv + 10)]
    ortacha_xona = round(yakin_uylar['Xonalar_Soni'].mean()) if not yakin_uylar.empty else "nomalum"

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=df, x='Kvadrat_Metr', y='Narxi_USD', color='#3498db', alpha=0.7, label="hand made house details: ")

    X_line = np.linspace(df['Kvadrat_Metr'].min(), df['Kvadrat_Metr'].max(), 100).reshape(-1, 1)
    y_line = model.predict(X_line)
    plt.plot(X_line, y_line, color='#e74c3c', linewidth=3, linestyle='--', label="linear regression")

    plt.scatter(user_kv, predicted_price, color='#2ecc71', marker='*', s=300, edgecolor='black', zorder=5,
                label=f"uyingiz ({user_kv} kv.m -> ${predicted_price:,.0f})")

    plt.title("Linear Regression: Uy Maydoni va Narxi O'rtasidagi Bog'liqlik", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Uy maydoni (kvadrat metr - kv.m)", fontsize=11)
    plt.ylabel("Uy narxi ($ USD)", fontsize=11)

    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['${:,.0f}'.format(x) for x in current_values])

    info_text = f"Kiritilgan maydon: {user_kv} kv.m\n Bashorat narx: ${predicted_price:,.2f}\n Taxminiy xonalar: {ortacha_xona} ta"
    plt.text(df['Kvadrat_Metr'].min() + 5, df['Narxi_USD'].max() - 40000, info_text,
             fontsize=11, bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5', edgecolor='#bdc3c7'))

    plt.legend(loc="lower right", frameon=True, fontsize=10)
    plt.tight_layout()

    plt.show()

except ValueError:
    print("error please insert valid number")