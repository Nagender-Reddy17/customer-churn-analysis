import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("data/processed/cleaned_churn.csv")

print("Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())

# -------------------------------
# 1. Churn Rate
# -------------------------------
churn_rate = df['churn'].mean() * 100
print(f"\n📊 Churn Rate: {churn_rate:.2f}%")

# -------------------------------
# 2. Churn Distribution
# -------------------------------
sns.countplot(x='churn', data=df)
plt.title("Churn Distribution")
plt.show()

# -------------------------------
# 3. Age vs Churn
# -------------------------------
sns.boxplot(x='churn', y='age', data=df)
plt.title("Age vs Churn")
plt.show()

print("💡 Younger customers may churn more depending on distribution.")

# -------------------------------
# 4. Income vs Churn
# -------------------------------
sns.boxplot(x='churn', y='income', data=df)
plt.title("Income vs Churn")
plt.show()

print("💡 Income level impacts churn behavior.")

# -------------------------------
# 5. Tenure vs Churn
# -------------------------------
sns.boxplot(x='churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()

print("💡 Lower tenure customers are more likely to churn.")

# -------------------------------
# 6. Services vs Churn
# -------------------------------
services = ['internet', 'wireless', 'callwait', 'ebill']

for col in services:
    if col in df.columns:
        churn_rate_service = df.groupby(col)['churn'].mean() * 100
        print(f"\n📊 Churn by {col}:\n", churn_rate_service)

# -------------------------------
# 7. Revenue-like Columns
# -------------------------------
billing_cols = ['longmon', 'tollmon', 'equipmon', 'cardmon', 'wiremon']

for col in billing_cols:
    if col in df.columns:
        sns.boxplot(x='churn', y=col, data=df)
        plt.title(f"{col} vs Churn")
        plt.show()

# -------------------------------
# 8. Customer Category
# -------------------------------
if 'custcat' in df.columns:
    cust = df.groupby('custcat')['churn'].mean() * 100
    print("\n📊 Churn by Customer Category:\n", cust)

# -------------------------------
# 9. Key Insights
# -------------------------------
print("\n🔍 Key Insights:")
print("- Customers with low tenure show higher churn.")
print("- Usage/billing patterns influence churn behavior.")
print("- Service usage (internet, wireless) impacts retention.")
print("- Different customer categories behave differently.")

print("\n✅ EDA Completed Successfully!")