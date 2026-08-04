import pandas as pd

df = pd.read_csv("data/Train_cleaned.csv")

print("\nCustomer Segmentation Summary\n")

print("Segment Distribution:")
print(df["Segmentation"].value_counts())

print("\nProfession Distribution:")
print(df["Profession"].value_counts())

print("\nSpending Score Distribution:")
print(df["Spending_Score"].value_counts())

print("\nAverage Age by Segment:")
print(df.groupby("Segmentation")["Age"].mean())

print("\nAverage Work Experience by Segment:")
print(df.groupby("Segmentation")["Work_Exp"].mean())