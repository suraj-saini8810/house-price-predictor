import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
from sklearn.tree import DecisionTreeRegressor    
import pickle

data = pd.read_csv("kc_house_data.csv")
dipt = data[["bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfront","sqft_above","sqft_basement","yr_built"]]
dout = data[["price"]]

x_train, x_test, y_train, y_test = train_test_split(dipt, dout, test_size=0.10, random_state=10)

lr = LinearRegression()  
lr.fit(x_train, y_train.values.ravel())
print("Score:", lr.score(x_test, y_test.values.ravel()))

with open("module.pickle", "wb") as f:
    pickle.dump(lr, f)
print("Model saved!")
