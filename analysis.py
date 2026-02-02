import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\Sales_Analysis\\vegetable.csv")

# Show first five rows of the dataframe
print('First five rows of the dataframe:')
print(df.head())

# Convert date column
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Handle missing city values
df['City'] = df['City'].fillna('Unknown')

# Create Revenue column
df['Revenue'] = df['Quantity_KG'] * df['Price_per_KG']

# Summary statistics
total_revenue = df['Revenue'].sum()
total_orders = df['OrderID'].nunique()
total_customers = df['CustomerID'].nunique()

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

# Sales by Vegetable
veg_sales = df.groupby('Vegetable')['Revenue'].sum().sort_values(ascending=False)

veg_sales.plot(kind='bar')
plt.title("Revenue by Vegetable")
plt.xlabel("Vegetable")
plt.ylabel("Revenue")
plt.show()

# Sales by Category
category_sales = df.groupby('Category')['Revenue'].sum()

category_sales.plot(kind='bar')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# Sales by City
city_sales = df.groupby('City')['Revenue'].sum().sort_values(ascending=False)

city_sales.plot(kind='bar')
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

# Payment Method Analysis
payment_sales = df.groupby('PaymentMethod')['Revenue'].sum()

payment_sales.plot(kind='bar')
plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")
plt.show()

# Monthly Sales Trend
monthly_sales = df.groupby(df['OrderDate'].dt.to_period('M'))['Revenue'].sum()
monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
