#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    print("Hello Data & AI!")

if __name__ == "__main__":
    main()


# In[3]:


numbers = [2, 4, 6, 8, 10]

for num in numbers:
    print(num * 2)


# In[4]:


transaction = {
    "Customer": "A001",
    "Product": "Milk",
    "Quantity": 2,
    "Price": 1.25
}

total_cost = transaction["Quantity"] * transaction["Price"]
print("Total Cost:", total_cost)


# In[11]:


import pandas as pd

# Create the raw sales data as a dictionary
data = {
    "Customer": ["A001", "A002", "A003", "A004", "A005"],
    "Product": ["Milk", "Bread", "Coffee", "Rice", "Chocolate"],
    "Quantity": [2, 1, 1, 2, 3],
    "Price": [1.25, 1.20, 4.00, 2.50, 2.30]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("sales.csv", index=False)

# 1. Load the CSV file
df = pd.read_csv("sales.csv")

# 2. Add a new column for Total = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]

# 3. Print total revenue (sum of Total)
total_revenue = df["Total"].sum()
print("Total Revenue:", total_revenue)

# 4. Find which product was bought the most (by total Quantity)
best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_selling_product)


# In[12]:


# sales_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales.csv")

# Create a bar chart: Product vs Quantity
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Quantity"], color="skyblue")
plt.title("Product vs Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)  # rotate product names for better readability
plt.tight_layout()
plt.show()


# In[ ]:




