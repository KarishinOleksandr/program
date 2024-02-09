import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
month_number = df["month_number"]
total_profit = df["total_profit"]

plt.figure(figsize=(8, 6))
plt.plot(month_number, total_profit, linestyle="--", marker="o", color="red", linewidth=3, label="Profit data of last year")
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company Sales data of last years")
plt.legend(loc="lower right")
plt.show()


df = pd.read_csv("sales_data.csv")
products = df.columns[1:-2]
plt.figure(figsize=(10, 6))

for product in products:
    plt.plot(df["month_number"], df[product], marker="o", label=product)
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Sales data")
plt.legend()
plt.grid(True)
plt.show()



df = pd.read_csv("sales_data.csv")

plt.figure(figsize=(8, 6))
plt.scatter(df["month_number"], df["toothpaste"])
plt.xlabel("Month Number")
plt.ylabel("Numeric of units sold")
plt.title("Toothpaste Sales data")
plt.grid(True, linestyle="--")
plt.show()


df = pd.read_csv("sales_data.csv")
plt.figure(figsize=(8, 6))

plt.bar(df["month_number"], df["facecream"], width=0.4, align="center", label="Face Cream sales data")
plt.bar(df["month_number"] + 0.4, df["facewash"], width=0.4, align="center", label="Face Wash sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Facewash and Facecream sales data")
plt.legend()
plt.grid(True)
plt.xticks(df["month_number"])
plt.show()

df = pd.read_csv("sales_data.csv")
total_sales = df.sum()[1:-2]

plt.figure(figsize=(8, 6))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Data")
plt.axis("equal")
plt.show()