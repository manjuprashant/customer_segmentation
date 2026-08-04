import pandas as pd

# Example: load Train dataset
train = pd.read_csv("Train.csv")

# Fix missing values safely
train['Profession'] = train['Profession'].fillna('Unknown')
train['Work_Experience'] = train['Work_Experience'].fillna(train['Work_Experience'].median())
train['Var_1'] = train['Var_1'].fillna('Cat_0')

# Repeat the same for Test dataset
test = pd.read_csv("Test.csv")
test['Profession'] = test['Profession'].fillna('Unknown')
test['Work_Experience'] = test['Work_Experience'].fillna(test['Work_Experience'].median())
test['Var_1'] = test['Var_1'].fillna('Cat_0')

# Save cleaned files
train.to_csv("Train_cleaned.csv", index=False)
test.to_csv("Test_cleaned.csv", index=False)
