
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 140, 130]


plt.figure(figsize=(14, 8))


plt.subplot(2, 2, 1)
plt.plot(months, sales, marker='o', linestyle='-', color='teal')
plt.title("Monthly Sales of Product X (Line)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True)


plt.subplot(2, 2, 2)
plt.barh(months, sales, color="lightblue")
plt.title("Monthly Sales (Bar)")
plt.xlabel("Units Sold")
plt.ylabel("Month")
plt.grid(axis='x', linestyle="--", alpha=0.5)


plt.subplot(2, 1, 2)
colors = ["purple", "green", "gold", "skyblue", "yellow", "pink", 
          "cyan", "orange", "red", "brown", "grey", "magenta"]
plt.pie(sales, labels=months, colors=colors[:len(months)], autopct="%.1f%%", startangle=140)
plt.title("Monthly Sales Distribution (Pie)")


plt.tight_layout()
plt.show()
