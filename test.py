import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # ploting , visualization
import seaborn as sns # ploting
from sklearn import model_selection #scikit learn
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing
from sklearn import utils
from sklearn import feature_selection
import warnings
import pickle
warnings.filterwarnings("ignore")
df= pd.read_csv("e:/C/datasets_12603_17232_Life Expectancy Data.csv")
df.head()
df.isnull().sum()
df=df.dropna()
X=df.drop(["Year","Country","Status","Life expectancy "],axis=1)
Y=df['Life expectancy ']
Y=Y.astype('int')
X=X.astype('int')
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.25, random_state=42)
l=linear_model.LinearRegression()
l.fit(Xtrain,Ytrain)
pickle.dump(l,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rbs'))

