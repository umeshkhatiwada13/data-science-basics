import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/umeshkhatiwada13/Datasets/main/healthcare-dataset-stroke-data_5k.csv")

print(df.head())

# drop id column
df.drop('id', axis=1, inplace=True)

print(df.head())

print(df.describe())

print(df.info())

print(df.isna().sum())

print("BMI mode is", df['bmi'].mode()[0])
print("BMI median is", df['bmi'].median())

df['bmi'] = df['bmi'].fillna(df['bmi'].median())

print(df.isna().sum())

