import pandas as pd
import numpy as np

#df=pd.read_csv(r"C:\Users\Karthik\OneDrive\Documents\Analytics_Project\Sales_Dataset.csv")
df=pd.read_csv('Sales_Dataset.csv')
print('Top 10 rows:\n',df.head(10))
print('About dataset:\n')
df.info()
print('\nStatistics:\n',df.describe())
print(df.columns)

print('\nMissing values:\n',df.isnull().sum())
df=df.drop_duplicates()
print('\nAfter removing duplicates:\n',df.shape)

numeric_cols=df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())


text_cols=df.select_dtypes(include=['object']).columns
for col in text_cols:
    m = df[col].mode()
    if len(m) > 0:
        df[col] = df[col].fillna(m.iloc[0])
    else:
        df[col] = df[col].fillna('Unknown')

df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
text_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower=q1 - 1.5 * iqr
    upper=q3 + 1.5 * iqr
    df=df[(df[col] >= lower) & (df[col] <= upper)]

print('\nCleaned dataset shape:\n',df.shape)

df.to_csv(r"C:\Users\Karthik\OneDrive\Documents\Analytics_Project\Sales_Dataset_Cleaned.csv", index=False)
print('\nCleaned dataset saved to Sales_Dataset_Cleaned.csv')



