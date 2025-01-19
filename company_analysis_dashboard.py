# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up Streamlit page configuration
st.set_page_config(page_title="Company Financial Dashboard", layout="wide")

# Sample financial data
data_income = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Revenue": [500000, 600000, 550000, 650000, 700000],
    "COGS": [200000, 250000, 220000, 260000, 280000],
    "Operating Expenses": [100000, 120000, 110000, 130000, 140000],
    "Net Income": [200000, 230000, 220000, 260000, 280000]
}

data_balance = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Total Assets": [1000000, 1100000, 1050000, 1150000, 1200000],
    "Total Liabilities": [400000, 450000, 430000, 460000, 470000],
    "Shareholder Equity": [600000, 650000, 620000, 690000, 730000],
    "Current Assets": [300000, 320000, 310000, 330000, 340000],
    "Current Liabilities": [100000, 120000, 110000, 130000, 140000]
}

# Converting dictionaries to DataFrames
income_df = pd.DataFrame(data_income)
balance_df = pd.DataFrame(data_balance)

# Financial analysis calculations
income_df['Gross Profit Margin'] = (income_df['Revenue'] - income_df['COGS']) / income_df['Revenue']
income_df['Net Profit Margin'] = income_df['Net Income'] / income_df['Revenue']
balance_df['Current Ratio'] = balance_df['Current Assets'] / balance_df['Current Liabilities']
balance_df['ROA'] = income_df['Net Income'] / balance_df['Total Assets']
balance_df['ROE'] = income_df['Net Income'] / balance_df['Shareholder Equity']
income_df['Revenue Growth (%)'] = income_df['Revenue'].pct_change() * 100
income_df['Net Income Growth (%)'] = income_df['Net Income'].pct_change() * 100

#  Streamlit layout
st.title("Company Financial Performance Dashboard")
st.sidebar.title("Dashboard Options")

# Sidebar filters
selected_years = st.sidebar.multiselect("Select Years to View", options=income_df['Year'], default=income_df['Year'])
filtered_income = income_df[income_df['Year'].isin(selected_years)]
filtered_balance = balance_df[balance_df['Year'].isin(selected_years)]

# Main dashboard
st.subheader("Income Statement Metrics")
st.dataframe(filtered_income)

st.subheader("Balance Sheet Metrics")
st.dataframe(filtered_balance)

# Visualizations
st.subheader("Visualizations")

# Revenue and Net Income Plot
st.write("### Revenue and Net Income Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_income, x="Year", y="Revenue", marker="o", label="Revenue")
sns.lineplot(data=filtered_income, x="Year", y="Net Income", marker="o", label="Net Income")
plt.title("Revenue and Net Income")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
st.pyplot(fig)

# Ratios Plot
st.write("### Ratios Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_balance, x="Year", y="Current Ratio", marker="o", label="Current Ratio")
sns.lineplot(data=filtered_balance, x="Year", y="ROA", marker="o", label="ROA")
sns.lineplot(data=filtered_balance, x="Year", y="ROE", marker="o", label="ROE")
plt.title("Liquidity and Profitability Ratios")
plt.xlabel("Year")
plt.ylabel("Ratio")
plt.legend()
st.pyplot(fig)

st.write("Dashboard created using Streamlit!")
