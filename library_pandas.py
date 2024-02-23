import pandas as pd

#Creating and Exploring a DataFrame:
#Use Case: You have data about different fruits and their prices which you want to organize
# and explore.

data={
    'Fruit':['Apple','Banana','Orange'],
    'Sales':[12,5,4]
}

df=pd.DataFrame(data)
print(df)

#Basic Data Analysis:
#Use Case: You want to get some basic statistics from your data, like the average price of the fruits.

mean_price=df['Sales'].mean()
print(mean_price)

#Handling Missing Data:
#Use Case: Some data in your DataFrame is missing,
#and you need to handle this for accurate analysis.

df['Quantity']=pd.Series([10,None,5])
df.fillna({'Quantity':0},inplace=True)
print(df)
