# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame creation (you can replace this with actual data from a CSV or other source)
data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Order_Date': ['2023-01-05', '2023-01-07', '2023-01-10', '2023-01-15', '2023-01-20', 
                   '2023-01-25', '2023-01-30', '2023-02-01', '2023-02-05', '2023-02-10'],
    'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Furniture', 
                         'Furniture', 'Clothing', 'Electronics', 'Clothing', 'Furniture'],
    'Sales_Amount': [250, 120, 310, 150, None, 400, 130, 500, 160, 600]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Convert 'Order_Date' to datetime for better analysis
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Handling missing values: Filling missing 'Sales_Amount' with the mean
df['Sales_Amount'].fillna(df['Sales_Amount'].mean(), inplace=True)

# 1. Summary statistics of the sales data
summary = df.groupby('Product_Category')['Sales_Amount'].agg(['mean', 'median', 'sum'])
print("Summary Statistics:\n", summary)

# 2. Total sales per category
total_sales_by_category = df.groupby('Product_Category')['Sales_Amount'].sum()
print("\nTotal Sales by Category:\n", total_sales_by_category)

# 3. Sales trend over time (group by date and sum sales amount)
sales_trend = df.groupby('Order_Date')['Sales_Amount'].sum()
print("\nSales Trend Over Time:\n", sales_trend)

# 4. Visualizing the results

# Bar chart for total sales by product category
plt.figure(figsize=(10, 6))
total_sales_by_category.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()

# Line chart for sales trend over time
plt.figure(figsize=(10, 6))
sales_trend.plot(kind='line', marker='o', color='purple')
plt.title('Sales Trend Over Time')
plt.xlabel('Order Date')
plt.ylabel('Sales Amount')
plt.grid(True)
plt.show()
