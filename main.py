import pandas as pd

df = pd.read_csv("data/countries.csv")

country = input("Country: ")

result = df[df["country"] == country]

if len(result) > 0:
    aging_rate = result.iloc[0]["aging_rate"]

    print(f"Country: {country}")
    print(f"Aging Rate: {aging_rate}%")
    print()

    print("Recommended Industries:")

    if aging_rate >= 25:
        print("- Healthcare")
        print("- Silver Industry")
        print("- Medical Devices")
        report = """
Analysis Report:
This country has a very high aging rate.
Healthcare services, medical devices, and senior-focused industries
are likely to experience strong growth in the future.
"""

    elif aging_rate >= 15:
        print("- Healthcare")
        print("- Automation")
        print("- Insurance")
        report = """
Analysis Report:
This country is experiencing a noticeable aging trend.
Demand for healthcare, automation, and insurance services
is expected to increase as the population structure changes.
"""

    else:
        print("- Education")
        print("- Consumer Goods")
        print("- Technology")
        report = """
Analysis Report:
This country still has a relatively young population.
Education, technology, and consumer markets may continue
to expand in the coming years.
"""

else:
    print("Country not found.")


print()
print(report)