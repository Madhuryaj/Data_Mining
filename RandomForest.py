import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error,r2_score

# load data
df = pd.DataFrame({
    'Salary': [1000, 1500, 2000, 2500, 3000, 500, 1000, 1250, 1750, 2000, 1000, 1500, 2000, 2500, 3000, 500, 1000, 1250, 1750, 2000],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female','Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Exp': [2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8]
})

df=pd.get_dummies(df,drop_first=True)

#Separate the features (Gender, Exp) and the target variable (Salary)
X=df.drop(['Salary'],axis=1)
y=df['Salary']

#Split the data into train and test sets (80:20)
X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#DeIne the random forest model and It the RF model on the train data
rf_model=RandomForestRegressor(random_state=42)
rf_model.fit(X_train,y_train)

y_pred=rf_model.predict(X_test)
print("Test R2 Score" ,r2_score(y_test,y_pred))
print("MSE Score",mean_squared_error(y_test,y_pred))

#Obtain the feature importances and plot them
import matplotlib.pyplot as plt
importance=pd.Series(rf_model.feature_importances_,index=X.columns)

print(importance)

importance.plot(kind='barh')
plt.show()

#DeIne the RF model with OOB, It the RF model using the train data, evaluate the OOB
#scores, and plot the feature importance


rf_model_withoob=RandomForestRegressor(random_state=42,oob_score=True)
rf_model_withoob.fit(X_train,y_train)

print('OOB R2 Score',rf_model_withoob.oob_score_)
print('OOB MSE Score',mean_squared_error(y_train,rf_model_withoob.oob_prediction_))

#obtain the important features and plot them
importance=pd.Series(rf_model_withoob.feature_importances_,index=X.columns)
print(importance)
importance.plot(kind='barh')
plt.show()

#DeIne the hyperparameters to tune (number of trees)
param_grid={'n_estimators':[5,10,15,20]}

#DeIne the scoring metric
scoring={  'R2':'r2','MSE':'neg_mean_squared_error'}
print(scoring)

#Perform the Grid Search with cross-validation

grid_search=GridSearchCV(rf_model,param_grid=param_grid,cv=5,scoring=scoring,refit='R2')
grid_search.fit(X_train,y_train)

#Evaluate the model on the test data set
y_pred=grid_search.predict(X_test)
print('Test R2 Scores',r2_score(y_test,y_pred))
print('Test MSE Scores',mean_squared_error(y_test,y_pred))

#Display the best hyperparameters and corresponding R2 and MSE scores
print("Best hyperparameters",grid_search.best_params_)
print("Best R2 Score",grid_search.best_score_)
print("Best MSE Score",abs(grid_search.cv_results_['mean_test_MSE'][grid_search.best_index_]))

#Obtain the feature importances and plot them

#Diaplay the decision tree
from sklearn.tree import plot_tree

fig, ax = plt.subplots(figsize=(16, 8))
plot_tree(grid_search.best_estimator_[0], ax=ax, feature_names=X_train.columns)
plt.show()
