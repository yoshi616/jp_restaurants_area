import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    [2013,27000,17000,6700,2900,700,250,150,55000],
    [2015,45300,25100,12400,3100,1850,600,300,89000],
    [2017,69300,25300,14600,4600,2400,950,350,118000],
    [2019,101000,29400,14800,6100,3400,1000,500,156000],
    [2021,100900,31200,16400,6100,2500,1300,700,159000],
    [2023,122000,28600,19400,12900,2500,1300,690,187000],
    [2025,112400,29400,19200,15300,2800,1600,800,181000],
], columns=[
    "year","asia","north_america","europe","latin_america",
    "oceania","middle_east","africa","total"
])

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(11, 8), sharex=True,
    gridspec_kw={"height_ratios": [2.2, 1.2]}
)

# 上段：全体像
colors = ["#5a5a5a", "#7a7a7a", "#9a9a9a", "#b0b0b0", "#c2c2c2", "#d2d2d2", "#e0e0e0"]
ax1.stackplot(
    df["year"],
    df["asia"],
    df["north_america"],
    df["europe"],
    df["latin_america"],
    df["oceania"],
    df["middle_east"],
    df["africa"],
    labels=["アジア","北米","欧州","中南米","オセアニア","中東","アフリカ"],
    colors=colors,
    edgecolor="black",
    linewidth=0.4,
    alpha=0.95
)
ax1.plot(df["year"], df["total"], color="black", linewidth=1.6, marker="o", label="Total")
ax1.set_title("海外における日本食レストラン数（地域別）")
ax1.set_ylabel("店舗数")
ax1.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.5)
ax1.legend(ncol=2, frameon=False, fontsize=9, loc="upper left")

# 下段：上の機微を見る
line_styles = {
    "latin_america": ("solid", "o"),
    "oceania": ("dashed", "s"),
    "middle_east": ("dashdot", "^"),
    "africa": ("dotted", "D"),
}
gray_lines = {
    "latin_america": "#4d4d4d",
    "oceania": "#777777",
    "middle_east": "#9a9a9a",
    "africa": "#b5b5b5",
}

for col, label in [
   ("latin_america", "中南米"),
    ("oceania", "オセアニア"),
    ("middle_east", "中東"),
    ("africa", "アフリカ"),
]:
    ls, mk = line_styles[col]
    ax2.plot(
        df["year"], df[col],
        linestyle=ls, marker=mk, linewidth=1.8,
        color=gray_lines[col], label=label
    )

ax2.set_ylabel("店舗数")
ax2.set_xlabel("年")
ax2.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.5)
ax2.legend(frameon=False, ncol=2, fontsize=9, loc="upper left")

plt.tight_layout()
plt.show()
plt.savefig("jp_restaurants_area.png", dpi=300, bbox_inches="tight")