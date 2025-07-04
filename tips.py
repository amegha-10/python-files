
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")
Fig, axs = plt.subplots(2, 2, figsize=(12, 10))


axs[0, 0].hist(df['total_bill'], bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Histogram of Total Bill')
axs[0, 0].set_xlabel('Total Bill')
axs[0, 0].set_ylabel('Frequency')


axs[0, 1].boxplot(df['tip'], vert=True)
axs[0, 1].set_title('Boxplot of Tips')
axs[0, 1].set_ylabel('Tip Amount')


gender_counts = df['sex'].value_counts()
axs[1, 0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
axs[1, 0].set_title('Gender Distribution')


avg_total_bill = df.groupby('day')['total_bill'].mean()
axs[1, 1].bar(avg_total_bill.index, avg_total_bill.values, color='lightgreen')
axs[1, 1].set_title('Average Total Bill by Day')
axs[1, 1].set_xlabel('Day')
axs[1, 1].set_ylabel('Avg Total Bill')

plt.tight_layout()
plt.show()
