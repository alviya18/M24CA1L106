#Write a program to display bar chart, horizontal bar and pie chart of the sample data in Ndarray.
import numpy as np
import matplotlib.pyplot as plt
data = np.array([25, 15, 30, 10, 20])
labels = ['Mango', 'Apple', 'Grapes', 'Orange', 'Kiwi']

plt.bar(labels, data)
plt.xlabel('Fruits')
plt.ylabel('People')
plt.title('Bar Chart on how many people like each fruit')
plt.show()

plt.barh(labels, data)
plt.ylabel('Fruits')
plt.xlabel('People')
plt.title('Horizontal Bar Chart on how many people like each fruit')
plt.show()

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart on how many people like each fruit')
plt.show()


