from math import sqrt
import numpy as np
# import matplotlib.pyplot as plt
import warnings 
import random
from matplotlib import style
from collections import Counter
import pandas as pd 
# style.use('fivethirtyeight')
# dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
# new_features = [5,7]
# [[plt.scatter(ii[0],ii[1],color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0],new_features[1])
# plt.show()

def k_near_neirhbours(data, predict, k =3):
	if len(data) >= k:
		warnings.warn('lol')
	distances = []
	for group in data:
		for features in data[group]:
			euclidean_dist = np.linalg.norm(np.array(features) - np.array(predict))
			distances.append([euclidean_dist, group])
	votes  = [i[1] for i in sorted(distances)[:k]]
	vote_result = Counter(votes).most_common(1)[0][0]
	return vote_result
# result = k_near_neirhbours(dataset,new_features,k=3)
# print(result)
df = pd.read_csv('dataknear2.data')
df.replace('?',-99999, inplace = True)
df.drop(['id'], 1, inplace = True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)
test_size = 0.2

train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]
# print(train_data[:10])
for i in train_data:
	train_set[i[-1]].append(i[:-1])

for i in test_data:
	test_set[i[-1]].append(i[:-1])

correct = 0
total = 0
for group in test_set:
	for data in test_set[group]:
		vote = k_near_neirhbours(train_set,data, k=5)
		if group==vote:
			correct+=1
		total+=1
print("Accuracy : ", correct/total)
