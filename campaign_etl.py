import pandas as pd

# CSV load
df = pd.read_csv(r"C:\Users\hsays\OneDrive\Desktop\New Folder\data.csv")

# Basic cleaning
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

print(df.head())
# Advanced Metrics (IMPORTANT 🔥)

# CTR
df["CTR"] = (df["clicks"] / df["impressions"]) * 100

# CPC
df["CPC"] = df["spent"] / df["clicks"]

# Conversion Rate
df["Conversion_Rate"] = (df["total_conversion"] / df["clicks"]) * 100

# Handle division issues
df["CPC"] = df["CPC"].fillna(0)
df["Conversion_Rate"] = df["Conversion_Rate"].replace([float("inf")], 0)
df.to_csv(r"C:\Users\hsays\OneDrive\Desktop\cleaned_campaign_data.csv", index=False)
print("Final CSV saved!")
print("Data cleaned successfully!")
print("Metrics added successfully!")
print(df.head())