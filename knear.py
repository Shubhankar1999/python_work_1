import numpy as np 
from sklearn import preprocessing,model_selection, neighbors
import pandas as pd 

df = pd.read_csv('dataknear2.data')
df.replace('?',-99999, inplace = True) 
 ## replace missing data denoted by ? with a number

df.drop(['id'],1,inplace = True)

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train,y_test = model_selection.train_test_split(X,y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()

clf.fit(X_train,y_train)

accur = clf.score(X_test,y_test)
print(accur)

example_row = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_row = example_row.reshape(len(example_row),-1) # reshape for scikit learn
prediction = clf.predict(example_row)
print(prediction)