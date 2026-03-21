import pandas as pd
import plotly.express as px

df_country = pd.DataFrame([
    [2023, "France", 4680],
    [2023, "Russia", 3190],
    [2023, "Italy", 2460],
    [2023, "United Kingdom", 1260],
    [2023, "Netherlands", 1180],
    [2023, "Germany", 1220],
    [2023, "Poland", 870],
    [2023, "Spain", 700],
    [2023, "Switzerland", 270],
    [2023, "Sweden", 530],
    [2023, "Belgium", 150],
    [2023, "Czechia", 300],
    [2023, "China", 78760],
    [2023, "South Korea", 18210],
    [2023, "Taiwan", 7440],
    [2023, "Thailand", 5330],
    [2023, "Malaysia", 1890],
    [2023, "United States", 26040],
    [2023, "Canada", 2610],
    [2023, "Mexico", 7120],
    [2023, "Brazil", 2850],
    [2023, "Australia", 2000],

    [2025, "France", 3390],
    [2025, "Russia", 2520],
    [2025, "Italy", 2160],
    [2025, "United Kingdom", 1820],
    [2025, "Netherlands", 1550],
    [2025, "Germany", 1510],
    [2025, "Poland", 890],
    [2025, "Spain", 810],
    [2025, "Switzerland", 380],
    [2025, "Sweden", 310],
    [2025, "Belgium", 170],
    [2025, "Czechia", 330],
], columns=["year", "country", "restaurants"])

fig = px.choropleth(
    df_country,
    locations="country",
    locationmode="country names",
    color="restaurants",
    hover_name="country",
    hover_data={"restaurants": ":,"},
    animation_frame="year",
    color_continuous_scale="Reds",
    projection="natural earth",
    title="Japanese Restaurants Overseas by Country (Major Countries)"
)

fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
fig.show()