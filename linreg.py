import pandas
import quandl as qd
import math
import numpy as np
import sklearn
from sklearn import preprocessing, model_selection,svm
from sklearn.linear_model import LinearRegression
print("hello")
print('The scikit-learn version is {}.'.format(sklearn.__version__))
#df = qd.get('WIKI/GOOGL')

df = pandas.DataFrame(np.random.randint(low=0, high=10, size=(50, 5)),
	columns=['Close', 'Open', 'c', 'd', 'e'])
df.fillna(-99999,inplace=True)
print(df.head())
X = np.array(df.drop(['Close'],1))
y = np.array(df['Close'])

X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size = 0.9)

clf = LinearRegression()

clf.fit(X_train,y_train)
accr = clf.score(X_test,y_test)
print(accr)