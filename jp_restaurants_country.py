import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame([
    ["France", 4680, 3390],
    ["Italy", 2460, 2160],
    ["United Kingdom", 1260, 1820],
    ["Netherlands", 1180, 1550],
    ["Germany", 1220, 1510],
    ["Poland", 870, 890],
    ["Spain", 700, 810],
    ["Switzerland", 270, 380],
    ["Sweden", 530, 310],
    ["Belgium", 150, 170],
    ["Czechia", 300, 330],
], columns=["country", "y2023", "y2025"])

df = df.sort_values("y2025")

y = np.arange(len(df))
h = 0.36

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    y - h/2, df["y2023"],
    height=h,
    color="white",
    edgecolor="black",
    label="2023"
)

ax.barh(
    y + h/2, df["y2025"],
    height=h,
    color="#7a7a7a",
    edgecolor="black",
    label="2025"
)

ax.set_yticks(y)
ax.set_yticklabels(df["country"])
ax.set_xlabel("Number of restaurants")
ax.set_title("Japanese Restaurants in Major European Countries: 2023 vs 2025")
ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.5)
ax.legend(frameon=False)

plt.tight_layout()
plt.show()
plt.savefig("jp_restaurants_country.png", dpi=300, bbox_inches="tight")