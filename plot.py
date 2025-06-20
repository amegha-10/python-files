
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 140, 130]


plt.plot(months, sales, marker='o', linestyle='-', color='teal')


plt.title("Monthly Sales of Product X")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.grid(True)
plt.tight_layout()

plt.show()
