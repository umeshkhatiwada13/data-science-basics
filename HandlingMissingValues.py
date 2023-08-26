import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:/Users/Umesh/Desktop/Sem 1/Data Science and Machine Learning 1114/mimic-iii-clinical-database-demo-1.4/PATIENTS.csv",
    parse_dates=['dob', 'dod'])

df['age'] = df['dod'].dt.year - df['dob'].dt.year
print(df.head())

print("Mean : ", df['age'].mean())
print("Median : ", df['age'].median())
print("Min : ", df['age'].min())
print("Max : ", df['age'].max())
print("Mode : ", df['age'].mode()[0])

print(df['age'].mean())

plt.hist(df['age'])
plt.show()

df1 = pd.read_csv(
    "C:/Users/Umesh/Desktop/Sem 1/Data Science and Machine Learning 1114/mimic-iii-clinical-database-demo-1.4/PATIENTS.csv",
    usecols=['hadm_id', 'charttime', 'itemid', 'valuenum'])

df1_pivoted = pd.pivot_table()
