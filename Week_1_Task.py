""" Lab Exercise: Sales Analysis (30 mints)
Objective: Analyse sales data and calculate key metrics using Python.
Dataset: Assume you have a dataset containing daily sales for a given month. The
dataset is a list of integers representing daily sales figures.
sales_data = [1200, 1500, 1800, 2000, 1600, 2200, 2400, 2100, 1900, 2000, 2300,
2500, 1700, 2200, 2000, 1800, 1900, 2100, 2300, 2400, 2500, 2000, 1800, 1600, 1500]
Tasks:
1. Calculate and print the total sales for the month.
2. Determine the average daily sales and print it.
3. Identify and print the highest and lowest sales days.
4. Check if the sales on the 10th day exceed 2000; print a message accordingly.
5. Use a ternary operator to print "Good" if the total sales are above 50,000; otherwise, print
“Average“.
6. Create a new list containing only the days where sales exceeded 2000.
Hints:
• Use a for loop to iterate through the sales data.
• Utilise conditional statements to check specific conditions.
• Apply arithmetic operators for calculations.
• Employ the ternary operator for concise conditional expressions.
• Functions: sum(), len(), min(), max().
"""
# data set
sales_data = [1200, 1500, 1800, 2000, 1600, 2200, 2400, 2100, 1900, 2000,
              2300, 2500, 1700, 2200, 2000, 1800, 1900, 2100, 2300, 2400, 2500, 2000,
              1800, 1600, 1500]

# Task 1: Calculate and print total sales
print("Total Sales of the month:", sum(sales_data))

# Task 2: Calculate and print average daily sales
print("Average Sales of the month:", sum(sales_data) / len(sales_data))

# Task 3: Identify and print highest and lowest sales days
print("Higest Sales", max(sales_data), "and Lowest Sales", min(sales_data))

# Task 4: Check if sales on the 10th day exceed 2000
if sales_data[9] > 2000:
    print("Yes sales exceeded 2000")
else:
    print("Sales was equal or below 2000")

# Task 5: Use a ternary operator to print "Good" or "Average"
print("Good" if sum(sales_data) > 50000 else "Average")

# Task 6: Create a new list with days where sales exceeded 2000
new_list = []
for i in sales_data:
    if i > 2000:
        new_list.append(i)
print(new_list)
