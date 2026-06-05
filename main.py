import pandas as pd

# Load country data
df = pd.read_csv("data/countries.csv")

# User input
country = input("Country: ")

# Search country
result = df[df["country"] == country]

if len(result) > 0:
    aging_rate = result.iloc[0]["aging_rate"]

    print(f"Country: {country}")
    print(f"Aging Rate: {aging_rate}%")
    print()

    print("Recommended Industries:")

    if aging_rate >= 25:
        industries = [
            "Healthcare",
            "Silver Industry",
            "Medical Devices"
        ]

        report = f"""
Analysis Report:
{country} has a very high aging rate.

Healthcare services, medical devices, and senior-focused industries
are likely to experience strong growth in the future.

The increasing elderly population may create new business opportunities
in healthcare, elderly care, and age-friendly technologies.
"""

    elif aging_rate >= 15:
        industries = [
            "Healthcare",
            "Automation",
            "Insurance"
        ]

        report = f"""
Analysis Report:
{country} is experiencing a noticeable aging trend.

Demand for healthcare, automation, and insurance services
is expected to increase as the population structure changes.

Businesses that improve productivity and support an aging workforce
may benefit from this demographic shift.
"""

    else:
        industries = [
            "Education",
            "Consumer Goods",
            "Technology"
        ]

        report = f"""
Analysis Report:
{country} still has a relatively young population.

Education, technology, and consumer markets may continue
to expand in the coming years.

A growing young population can support innovation,
workforce growth, and consumer demand.
"""

    for industry in industries:
        print(f"- {industry}")

    print(report)

else:
    print("Country not found.")