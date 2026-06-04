import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

# ==============================
# Dataset Overview
# ==============================
print("=" * 50)
print("E-COMMERCE KPI ANALYSIS DASHBOARD")
print("=" * 50)

print("\nDataset Preview:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# ==============================
# KPI Calculations
# ==============================
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_order_value = total_sales / total_orders

print("\n" + "=" * 50)
print("KEY PERFORMANCE INDICATORS (KPIs)")
print("=" * 50)

print(f"Total Sales: ₹{total_sales:,}")
print(f"Total Profit: ₹{total_profit:,}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{average_order_value:.2f}")

# ==============================
# Sales by Region
# ==============================
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

best_region = region_sales.idxmax()

# Bar Chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()

# ==============================
# Sales by Category
# ==============================
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

best_category = category_sales.idxmax()

# Pie Chart
plt.figure(figsize=(6, 6))
category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Category Contribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_contribution.png")
plt.show()

# ==============================
# Profit by Category
# ==============================
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit (₹)")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# ==============================
# Business Insights
# ==============================
print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)

print(f"Highest Performing Region: {best_region}")
print(f"Highest Selling Category: {best_category}")

print("\nKey Findings:")
print(f"• Total Revenue Generated: ₹{total_sales:,}")
print(f"• Total Profit Earned: ₹{total_profit:,}")
print(f"• Average Order Value: ₹{average_order_value:.2f}")
print(f"• Best Performing Region: {best_region}")
print(f"• Best Selling Category: {best_category}")

print("\nDashboard analysis completed successfully!")

# ==============================
# Save Results to TXT File
# ==============================

with open("analysis_report.txt", "w", encoding="utf-8") as file:

    file.write("=" * 50 + "\n")
    file.write("E-COMMERCE KPI ANALYSIS REPORT\n")
    file.write("=" * 50 + "\n\n")

    file.write("KEY PERFORMANCE INDICATORS\n")
    file.write("-" * 30 + "\n")

    file.write(f"Total Sales: ₹{total_sales:,}\n")
    file.write(f"Total Profit: ₹{total_profit:,}\n")
    file.write(f"Total Orders: {total_orders}\n")
    file.write(f"Average Order Value: ₹{average_order_value:.2f}\n\n")

    file.write("SALES BY REGION\n")
    file.write("-" * 30 + "\n")

    for region, sales in region_sales.items():
        file.write(f"{region}: ₹{sales:,}\n")

    file.write("\n")

    file.write("SALES BY CATEGORY\n")
    file.write("-" * 30 + "\n")

    for category, sales in category_sales.items():
        file.write(f"{category}: ₹{sales:,}\n")

    file.write("\n")

    file.write("BUSINESS INSIGHTS\n")
    file.write("-" * 30 + "\n")

    file.write(f"Best Performing Region: {best_region}\n")
    file.write(f"Best Selling Category: {best_category}\n")
    file.write(f"Total Revenue Generated: ₹{total_sales:,}\n")
    file.write(f"Total Profit Earned: ₹{total_profit:,}\n")

print("\nReport saved successfully as 'analysis_report.txt'")
