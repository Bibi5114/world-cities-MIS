import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Title
st.title("California Housing Data (1990) by Liu Yimeng")


# Load data
df = pd.read_csv("housing.csv")


# Slider: Minimal Median House Value
house_value_filter = st.slider(
    "Minimal Median House Value",
    0,
    500001,
    200000
)


# Sidebar subheader
st.subheader("See more filters in the sidebar:")


# Sidebar: Ocean proximity multiselect
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)


# Sidebar: Income level radio button
income_filter = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)


# Filter by median house value
df = df[
    df.median_house_value >= house_value_filter
]


# Filter by location type
df = df[
    df.ocean_proximity.isin(location_filter)
]


# Filter by income level
if income_filter == "Low":
    df = df[df.median_income <= 2.5]

elif income_filter == "Medium":
    df = df[
        (df.median_income > 2.5) &
        (df.median_income < 4.5)
    ]

else:
    df = df[df.median_income >= 4.5]


# Show map
st.subheader("Housing Locations")

st.map(
    df[
        ["latitude", "longitude"]
    ]
)


# Show histogram
st.subheader("Median House Value Distribution")


fig, ax = plt.subplots(figsize=(10, 5))

df.median_house_value.plot.hist(
    bins=30,
    ax=ax
)

ax.set_xlabel("Median House Value (USD)")
ax.set_ylabel("Number of Districts")

st.pyplot(fig)