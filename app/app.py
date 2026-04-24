import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Churn Analysis", layout="wide")

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("data/processed/cleaned_churn.csv")

st.title("📊 Customer Churn Analysis Dashboard")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filters")

tenure_range = st.sidebar.slider(
    "Select Tenure Range",
    int(df['tenure'].min()),
    int(df['tenure'].max()),
    (int(df['tenure'].min()), int(df['tenure'].max()))
)

custcat_filter = st.sidebar.multiselect(
    "Customer Category",
    options=df['custcat'].unique(),
    default=df['custcat'].unique()
)

df = df[(df['tenure'] >= tenure_range[0]) & 
        (df['tenure'] <= tenure_range[1])]

df = df[df['custcat'].isin(custcat_filter)]

# -------------------------------
# KPIs
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Churn Rate (%)", round(df['churn'].mean()*100,2))
col3.metric("Avg Tenure", round(df['tenure'].mean(),2))

st.markdown("---")

# -------------------------------
# Row 1: Distribution + Age
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='churn', data=df, palette=['green','red'], ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Age vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x='churn', y='age', data=df, palette=['blue','red'], ax=ax)
    st.pyplot(fig)

# -------------------------------
# Row 2: Income + Tenure
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Income vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x='churn', y='income', data=df, palette=['blue','red'], ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Tenure vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x='churn', y='tenure', data=df, palette=['blue','red'], ax=ax)
    st.pyplot(fig)

# -------------------------------
# Row 3: Service Analysis
# -------------------------------
st.subheader("Service Usage Impact")

services = ['internet', 'wireless', 'callwait', 'ebill']

for col in services:
    if col in df.columns:
        churn_rate = df.groupby(col)['churn'].mean()*100
        st.write(f"### {col.capitalize()} vs Churn")
        st.bar_chart(churn_rate)

# -------------------------------
# Row 4: Correlation Heatmap
# -------------------------------
st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include=['int64','float64'])
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap='coolwarm', annot=False, ax=ax)
st.pyplot(fig)

# -------------------------------
# Row 5: Scatter Plot
# -------------------------------
st.subheader("Income vs Tenure (Churn Highlight)")

fig, ax = plt.subplots()
sns.scatterplot(x='tenure', y='income', hue='churn', 
                palette={0:'blue',1:'red'}, data=df, ax=ax)
st.pyplot(fig)

# -------------------------------
# Insights Section
# -------------------------------
st.markdown("## 💡 Key Insights")

st.write("""
- Customers with low tenure are more likely to churn  
- Income and service usage influence churn behavior  
- Certain customer categories show higher churn rates  
- High-risk segments can be targeted for retention strategies  
""")
