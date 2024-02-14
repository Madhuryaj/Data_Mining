import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr

""" Create a dataframe with two variables """
data = {'X': [1.2, 2.1, 3.5, 4.7, 5.3], 'Y': [5.6, 4.1, 3.2, 2.8, 1.4]}
df = pd.DataFrame(data)

sns.scatterplot(x='X', y='Y', data=df)


