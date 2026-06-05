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

    elif aging_rate >= 15:
        print("- Healthcare")
        print("- Automation")
        print("- Insurance")

    else:
        print("- Education")
        print("- Consumer Goods")
        print("- Technology")

else:
    print("Country not found.")