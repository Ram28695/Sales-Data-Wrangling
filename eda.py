import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sales_Dataset_Cleaned.csv")

print(df.info())

print(df.describe())

# Categorical columns summary
print(df.describe(include='object'))

# Histograms for numerical columns
df.hist(figsize=(12,8))
plt.tight_layout()
plt.show( block=True)


# Correlation matrix
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show(block=True)

plt.figure(figsize=(8,6))
sns.scatterplot(x='amount', y='profit', data=df)
plt.title("Amount vs Profit")
plt.show(block=True)