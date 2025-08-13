import pandas as pd
import plotly.express as px
import plotly.io as pio
import warnings

# ===================== Ignore Future Warnings =====================
warnings.simplefilter(action='ignore', category=FutureWarning)

# ===================== Set Plotly to open charts in browser =====================
pio.renderers.default = 'browser'

# ===================== Load Dataset =====================
df = pd.read_csv("ecommerce_dataset_clean.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ===================== KPIs =====================
total_revenue = df['Total Amount'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = df['Total Amount'].mean()
num_customers = df['Customer ID'].nunique()

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")
print(f"Number of Customers: {num_customers}")

# ===================== Sales Over Time =====================
sales_over_time = df.groupby('Order Date')['Total Amount'].sum().reset_index()
fig1 = px.line(
    sales_over_time, x='Order Date', y='Total Amount',
    title='Sales Over Time', markers=True
)
fig1.update_layout(xaxis_title='Date', yaxis_title='Revenue (₹)')
fig1.show()

# ===================== Revenue by Product Category =====================
category_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()
fig2 = px.bar(
    category_sales, x='Total Amount', y='Product Category',
    orientation='h', title='Revenue by Product Category',
    text='Total Amount', color='Total Amount', color_continuous_scale='Viridis'
)
fig2.update_layout(xaxis_title='Revenue (₹)', yaxis_title='Category')
fig2.show()

# ===================== Revenue by Region =====================
region_sales = df.groupby('Region')['Total Amount'].sum().reset_index()
fig3 = px.bar(
    region_sales, x='Total Amount', y='Region',
    orientation='h', title='Revenue by Region',
    text='Total Amount', color='Total Amount', color_continuous_scale='Cividis'
)
fig3.update_layout(xaxis_title='Revenue (₹)', yaxis_title='Region')
fig3.show()

# ===================== Payment Method Distribution =====================
payment_counts = df['Payment Method'].value_counts().reset_index()
payment_counts.columns = ['Payment Method', 'Count']
fig4 = px.pie(
    payment_counts, values='Count', names='Payment Method',
    title='Payment Method Distribution', hole=0.3
)
fig4.show()
