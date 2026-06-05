import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/countries.csv")

st.title("Population Impact AI Agent")

# Dashboard Overview

st.header("Dataset Overview")

num_countries = len(df)

avg_aging_rate = round(df["aging_rate"].mean(), 1)

highest_country = df.loc[df["aging_rate"].idxmax()]
lowest_country = df.loc[df["aging_rate"].idxmin()]

st.write(f"**Number of Countries:** {num_countries}")

st.write(f"**Average Aging Rate:** {avg_aging_rate}%")

st.write(
    f"**Highest Aging Rate:** "
    f"{highest_country['country']} "
    f"({highest_country['aging_rate']}%)"
)

st.write(
    f"**Lowest Aging Rate:** "
    f"{lowest_country['country']} "
    f"({lowest_country['aging_rate']}%)"
)

st.header("Top 10 Aging Countries")

top10 = df.sort_values(
    by="aging_rate",
    ascending=False
)[["country", "aging_rate"]].head(10)

st.dataframe(top10)

# Country dropdown
country = st.selectbox(
    "Select Country",
    sorted(df["country"].unique())
)

# Analyze button
if st.button("Analyze"):

    result = df[df["country"] == country]

    aging_rate = result.iloc[0]["aging_rate"]
    population = result.iloc[0]["population"]
    median_age = result.iloc[0]["median_age"]

    st.subheader("Country Information")

    st.write(f"**Country:** {country}")
    st.write(f"**Aging Rate:** {aging_rate}%")
    st.write(f"**Population:** {population:,}")
    st.write(f"**Median Age:** {median_age}")

    st.subheader("Recommended Industries")

    if aging_rate >= 25:

        industries = [
            "Healthcare",
            "Silver Industry",
            "Medical Devices"
        ]

        report = f"""
{country} has a very high aging rate.

Healthcare services, medical devices, and senior-focused industries
are likely to experience strong growth in the future.
"""

    elif aging_rate >= 15:

        industries = [
            "Healthcare",
            "Automation",
            "Insurance"
        ]

        report = f"""
{country} is experiencing a noticeable aging trend.

Demand for healthcare, automation, and insurance services
is expected to increase as the population structure changes.
"""

    else:

        industries = [
            "Education",
            "Consumer Goods",
            "Technology"
        ]

        report = f"""
{country} still has a relatively young population.

Education, technology, and consumer markets may continue
to expand in the coming years.
"""

    for industry in industries:
        st.write(f"- {industry}")

    st.subheader("Analysis Report")
    st.write(report)

    st.subheader("Country Aging Rate Comparison")
    st.bar_chart(
        df.set_index("country")["aging_rate"]
    )