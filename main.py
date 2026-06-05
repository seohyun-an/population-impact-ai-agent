import pandas as pd

# Load country data
df = pd.read_csv("data/countries.csv")

# User input
country = input("Country: ")

# Search country
result = df[df["country"] == country]

if len(result) > 0:

    # Extract demographic data
    aging_rate = result.iloc[0]["aging_rate"]
    population = result.iloc[0]["population"]
    median_age = result.iloc[0]["median_age"]

    # Display country information
    print(f"\nCountry: {country}")
    print(f"Aging Rate: {aging_rate}%")
    print(f"Population: {population:,}")
    print(f"Median Age: {median_age}")

    print("\nRecommended Industries:")

    if aging_rate >= 25:
        industries = [
            "Healthcare",
            "Silver Industry",
            "Medical Devices"
        ]

        report = f"""
Analysis Report:
{country} has a very high aging rate.

With a median age of {median_age}, the country faces significant demographic aging.

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

The country has a population of {population:,} people and a median age of {median_age}.

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

With a median age of {median_age}, the country maintains a comparatively young demographic structure.

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