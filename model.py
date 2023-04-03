import numpy as np 
import pandas as pd 
df_yield = pd.read_csv('yield_df.csv')
df_yield.shape
df_yield = df_yield.drop(['Unnamed: 0'], axis=1)
df_yield.head()
df_yield.groupby('Item').count()
df_yield.groupby(['Area'],sort=True)['hg/ha_yield'].sum().nlargest(10)
df_yield.groupby(['Item','Area'],sort=True)['hg/ha_yield'].sum().nlargest(10)
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
features=df_yield.loc[:, df_yield.columns != 'hg/ha_yield']
features = features.drop(['Year'], axis=1)
label=df_yield['hg/ha_yield']
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct1=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
print("Features:", features)
features=np.array(ct1.fit_transform(features))
features
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features[:,10]=le.fit_transform(features[:,10])
print("New Features:", features)
yield_df_onehot=pd.DataFrame(features)
yield_df_onehot["hg/ha_yield"]=label
yield_df_onehot.head()
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
features=scaler.fit_transform(features) 
from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(features, label, test_size=0.2, random_state=42)
test_df=pd.DataFrame(test_data,columns=yield_df_onehot.loc[:, yield_df_onehot.columns != 'hg/ha_yield'].columns) 
from sklearn.ensemble import ExtraTreesRegressor
clf=ExtraTreesRegressor()
model=clf.fit(train_data,train_labels)

import pickle
pickle.dump(model, open('model.pkl','wb'))