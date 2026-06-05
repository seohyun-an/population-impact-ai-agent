import pandas as pd

df = pd.read_csv("data/countries.csv")

country = input("Country: ")

result = df[df["country"] == country]

if len(result) > 0:
    aging_rate = result.iloc[0]["aging_rate"]

    print(f"Country: {country}")
    print(f"Aging Rate: {aging_rate}%")

else:
    print("Country not found.")