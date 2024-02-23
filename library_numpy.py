import numpy as np

#Creating and Using Arrays:
#Use Case: You have a list of numbers, and you want to perform calculations on them.

data=np.array([1,2,3,6,7])
print(data)

sq_numbers=data**2
print(sq_numbers)

#Basic Statistics: Use Case: You need to calculate the mean or standard deviation of a dataset.

ages=np.array([20,34,12,45,20,36])

mean_age=np.mean(ages)
std_dev_age=np.std(ages)

print(mean_age)
print(std_dev_age)

#Matrix Operations:

#Use Case: Working with matrices for linear algebra operations, common in many data mining algorithms.

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

product=np.dot(A,B)
print(product)
