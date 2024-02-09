import pandas as pd
import matplotlib.pyplot as plt
"""
# Зчитування даних з CSV-файлу у DataFrame
df = pd.read_csv("sales_data.csv")

# Відбір потрібних колонок для побудови графіка
month_number = df['month_number']
total_profit = df['total_profit']

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(month_number, total_profit, linestyle='--', marker='o', color='red', linewidth=3, label='Total Profit')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Dynamics of Total Profit for 12 Months')
plt.legend(loc='lower right')
plt.show()
"""

"""
# Зчитування даних з CSV-файлу у DataFrame
df = pd.read_csv("sales_data.csv")

# Відокремлення даних для кожного товару
products = df.columns[1:-2]  # Всі назви стовпців, які відповідають продуктам

# Побудова графіків для кожного товару
plt.figure(figsize=(10, 6))

for product in products:
    plt.plot(df['month_number'], df[product], marker='o', label=product)

plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Product Sales')
plt.legend()
plt.grid(True)
plt.show()
"""



"""
# Зчитування даних з CSV-файлу у DataFrame
df = pd.read_csv("sales_data.csv")

# Побудова точкового графіку для продажів зубної пасти
plt.figure(figsize=(8, 6))
plt.scatter(df['month_number'], df['toothpaste'])
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales per Month')
plt.grid(True, linestyle='--')
plt.show()
"""

"""
# Зчитування даних з CSV-файлу у DataFrame
df = pd.read_csv("sales_data.csv")

# Побудова порівняльних гістограм для обсягів продажу кремів для обличчя та засобів для вмивання обличчя
plt.figure(figsize=(8, 6))

# Гістограма для кремів для обличчя
plt.bar(df['month_number'], df['facecream'], width=0.4, align='center', label='Face Cream')

# Додавання гістограми для засобів для вмивання обличчя, зсуваючи стовпці для чіткості порівняння
plt.bar(df['month_number'] + 0.4, df['facewash'], width=0.4, align='center', label='Face Wash')

plt.xlabel('Month Number')
plt.ylabel('Sales Volume')
plt.title('Comparison of Face Cream and Face Wash Sales per Month')
plt.legend()
plt.grid(True)
plt.xticks(df['month_number'])  # Встановлення міток на осі Х для кожного місяця
plt.show()
"""



# Зчитування даних з CSV-файлу у DataFrame
df = pd.read_csv("sales_data.csv")

# Сумуємо загальний обсяг продажів для кожного товару
total_sales = df.sum()[1:-2]  # Відкидаємо перший стовпчик (month_number) та останні два (total_units, total_profit)

# Побудова кругової діаграми
plt.figure(figsize=(8, 6))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Percentage for Each Product')
plt.axis('equal')  # Забезпечує кругову форму діаграми
plt.show()
