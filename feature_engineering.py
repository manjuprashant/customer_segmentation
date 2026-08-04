import pandas as pd

df = pd.read_csv("data/Train_cleaned.csv")

# Age Category
def age_category(age):
    if age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    elif age <= 55:
        return "46-55"
    else:
        return "55+"

df["Age_Category"] = df["Age"].apply(age_category)

df.to_csv("data/Train_cleaned.csv", index=False)

print("Feature engineering completed.")