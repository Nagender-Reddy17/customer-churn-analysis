# Streamlit app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.title("📊 Customer Churn Dashboard")

df = pd.read_csv("data/processed/cleaned_churn.csv")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Churn Rate (%)", round(df['churn'].mean()*100,2))
col3.metric("Avg Tenure", round(df['tenure'].mean(),2))

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='churn', data=df, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Tenure vs Churn")
    fig, ax = plt.subplots()
    sns.boxplot(x='churn', y='tenure', data=df, ax=ax)
    st.pyplot(fig)

# Insight section
st.markdown("## 💡 Key Insights")
st.write("""
- Customers with low tenure churn more  
- Service usage affects churn  
- High-risk segments identified  
""")