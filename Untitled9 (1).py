#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Data Cleaning for Missing Values
import pandas as pd

data = {
    "InvoiceID": ["A001","A002","A003","A004","A005","A006","A007","A008","A009","A010",
                  "A011","A012","A013","A014","A015","A016","A017","A018","A019","A020"],
    "Customer": ["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female",
                 "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"],
    "Age": [22,35,29,40,31,None,50,23,38,26,44,33,29,41,36,28,32,45,39,30],  # Missing Age
    "Product": ["Milk","Bread","Eggs","Coffee","Rice","Chocolate","Juice","Milk","Bread","Rice",
                None,"Chocolate","Eggs","Juice","Milk","Rice","Coffee","Chocolate","Bread","Juice"], # Missing Product
    "Quantity": [2,1,12,1,2,3,2,1,2,1,2,2,6,3,1,2,1,1,3,2],
    "Total": [2.50,1.20,3.60,4.00,5.00,6.90,4.00,1.25,2.40,2.50,
              8.00,4.60,1.80,6.00,1.25,5.00,4.00,2.30,3.60,4.00]
}

df = pd.DataFrame(data)

# Show rows with missing values BEFORE cleaning
print("🔎 Rows with missing values BEFORE cleaning:\n")
print(df[df["Age"].isna() | df["Product"].isna()])

# Cleaning Step
avg_age = df["Age"].mean()
most_common_product = df["Product"].mode()[0]

df["Age"].fillna(avg_age, inplace=True)
df["Product"].fillna(most_common_product, inplace=True)

# rows AFTER cleaning
print("\n✅ Rows AFTER cleaning:\n")
print(df.loc[[5, 10]])  # rows that had missing values

df.to_excel("supermarket_sales_cleaned.xlsx", index=False)


# In[14]:


# Data Visualization
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_excel("supermarket_sales_cleaned.xlsx")

# 1. Bar chart: Product vs Quantity sold
plt.figure(figsize=(6,4))
df.groupby("Product")["Quantity"].sum().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Product vs Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.show()

# 2. Histogram: Age distribution
plt.figure(figsize=(6,4))
df["Age"].plot(kind="hist", bins=6, edgecolor="black", color="lightgreen")
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# 3. Bar chart: Gender vs Total spending
plt.figure(figsize=(6,4))
df.groupby("Customer")["Total"].sum().plot(kind="bar", color=["blue", "pink"], edgecolor="black")
plt.title("Gender vs Total Spending")
plt.xlabel("Gender")
plt.ylabel("Total Spending")
plt.show()


# In[16]:


# Data Analysis
import pandas as pd

# Load cleaned dataset
df = pd.read_excel("supermarket_sales_cleaned.xlsx")

# 1. Average Age of customers
avg_age = df["Age"].mean()
print(f"Average Age of customers: {avg_age:.2f}")

# 2. Total revenue
total_revenue = df["Total"].sum()
print(f"Total Revenue: {total_revenue:.2f}")

# 3. Best-selling product (by Quantity)
best_product = df.groupby("Product")["Quantity"].sum().idxmax()
best_qty = df.groupby("Product")["Quantity"].sum().max()
print(f"Best-selling product: {best_product} ({best_qty} units sold)")

# 4. Which gender spends more (by Total)
gender_spending = df.groupby("Customer")["Total"].sum()
top_gender = gender_spending.idxmax()
top_gender_spent = gender_spending.max()
print(f"Gender that spends more: {top_gender} (Total: {top_gender_spent:.2f})")


# In[ ]:




