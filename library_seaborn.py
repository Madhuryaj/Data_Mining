import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution Plots:

# Use Case: You want to visualize the distribution of a dataset, for instance, the distribution of ages in a population
age = np.random.normal(20, 10, 200)
# sns.histplot(age,kde=True)

# Heatmaps: #Use Case: You have a matrix of
# data and want to visualize patterns in it, such as correlation between different variables.
data = np.random.rand(10, 10)
# sns.heatmap(data)

# Pair Plots:
# Use Case: You want to explore relationships between all pairs of numerical variables in a dataset.

df = pd.DataFrame({'x': np.random.rand(20),
                   'y': np.random.rand(20),
                   'z': np.random.rand(20)})
sns.pairplot(df)
plt.show()


# try
data={
    1:[1,2,3],
    2:["Moni","Thanu","Both"]
}
df_1 = pd.DataFrame(data)

#print(df_1)
print(df_1.keys())
print(df_1.keys()**2)
