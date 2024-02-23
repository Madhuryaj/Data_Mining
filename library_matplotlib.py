import matplotlib.pyplot as plt

#Line Chart - Use Case: Plotting a line graph of, say, your monthly expenses
months=['JAN','FEB','MAR','APR','MAY']
expense=[100,300,230,450,145]
#plt.plot(months,expense)
plt.xlabel("Months")
plt.ylabel("Expense")
plt.title("Monthly Expense Graph")
#plt.show()

#Bar Chart - Use Case: Comparing different categories, like sales of different products
products=["Pen","Book","Laptop"]
sales=[20,70,12]
#plt.bar(products,sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")

#Scatter Plot: Use Case: To see the relationship between two variables, like height and weight of individuals

height = [150, 160, 165, 185, 170]
weight = [50, 60, 65, 85, 70]

plt.scatter(height,weight)


plt.show()
