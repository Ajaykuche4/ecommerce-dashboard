import pandas as pd
import plotly.express as px
import streamlit as st

# ===================== Load Clean Dataset =====================
df = pd.read_csv("ecommerce_dataset_clean.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ===================== Page Config =====================
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📊 E-Commerce Sales Dashboard")

# ===================== Sidebar Filters =====================
st.sidebar.header("Filters")

# Date filter
start_date = st.sidebar.date_input("Start Date", df['Order Date'].min())
end_date = st.sidebar.date_input("End Date", df['Order Date'].max())
df = df[(df['Order Date'] >= pd.to_datetime(start_date)) &
        (df['Order Date'] <= pd.to_datetime(end_date))]

# Region filter
regions = st.sidebar.multiselect("Select Regions", df['Region'].unique(), default=df['Region'].unique())
df = df[df['Region'].isin(regions)]

# Product Category filter
categories = st.sidebar.multiselect("Select Categories", df['Product Category'].unique(), default=df['Product Category'].unique())
df = df[df['Product Category'].isin(categories)]

# ===================== KPIs =====================
st.subheader("Key Performance Indicators (KPIs)")
total_revenue = df['Total Amount'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = df['Total Amount'].mean()
num_customers = df['Customer ID'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue (₹)", f"{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Avg Order Value (₹)", f"{avg_order_value:,.2f}")
col4.metric("Number of Customers", num_customers)

# ===================== Sales Over Time =====================
st.subheader("Sales Over Time")
sales_over_time = df.groupby('Order Date')['Total Amount'].sum().reset_index()
fig1 = px.line(sales_over_time, x='Order Date', y='Total Amount', markers=True, title="Sales Over Time")
st.plotly_chart(fig1, use_container_width=True)

# ===================== Revenue by Product Category =====================
st.subheader("Revenue by Product Category")
category_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()
fig2 = px.bar(category_sales, x='Total Amount', y='Product Category', orientation='h',
              text='Total Amount', color='Total Amount', color_continuous_scale='Viridis')
st.plotly_chart(fig2, use_container_width=True)

# ===================== Revenue by Region =====================
st.subheader("Revenue by Region")
region_sales = df.groupby('Region')['Total Amount'].sum().reset_index()
fig3 = px.bar(region_sales, x='Total Amount', y='Region', orientation='h',
              text='Total Amount', color='Total Amount', color_continuous_scale='Cividis')
st.plotly_chart(fig3, use_container_width=True)

# ===================== Payment Method Distribution =====================
st.subheader("Payment Method Distribution")
payment_counts = df['Payment Method'].value_counts().reset_index()
payment_counts.columns = ['Payment Method', 'Count']
fig4 = px.pie(payment_counts, values='Count', names='Payment Method', hole=0.3)
st.plotly_chart(fig4, use_container_width=True)
