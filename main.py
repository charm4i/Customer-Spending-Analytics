import pandas as pd

df = pd.read_csv("data/Ecommerce_Sales_Data_2024_2025.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

print("cleaned data preview")
print(df.head())

print("\n check missing values")
print(df.isnull().sum())

print("/n ==== Buisness KPIS =====")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = df["Sales"].mean()
profit_margin = (total_profit/total_sales) * 100

print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: {avg_order_value:,.2f}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

print("\n====Sales By Region====")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales.apply(lambda x: f"{x:,.2f}"))

print("\n====Profit By Region====")
region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print(region_profit.apply(lambda x: f"{x:,.2f}"))

print("\n====Profit Margin by Region====")
region_margin = (df.groupby("Region")[["Sales","Profit"]].sum())

region_margin["Profit Margin %"] = (region_margin["Profit"]/ region_margin["Sales"]) * 100
print(region_margin.round(2))

print("\n===== Profit by Category =====")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
print(category_profit.apply(lambda x: f"{x:,.2f}"))

print("\n====Profit Margin by Category====")
category_margin = (df.groupby("Category")[["Sales", "Profit"]].sum())
category_margin["Profit Margin %"] = (category_margin["Profit"] / category_margin["Sales"]) * 100

print(category_margin.sort_values("Profit Margin %", ascending=False).round(2))

print("\n====Average Profit by Discount Level====")
discount_analysis = (
    df.groupby("Discount")[["Sales","Profit"]]
    .mean()
    .sort_index()
)
print(discount_analysis.round(2))

print("n====Correlation Between discount and profit====")
correlation = df["Discount"].corr(df["Profit"])
print(f"Correlation: {correlation:.4f}")

print("\n==== Monthly Sales Trend ====")
monthly_sales = (
    df.groupby(["Year","Month"])["Sales"]
    .sum()
    .reset_index()
    .sort_values(["Year","Month"])
)
print(monthly_sales)

df.to_csv("cleaned_ecommerce_data.csv",index=False)
print("Cleaned dataset exported successfully.")