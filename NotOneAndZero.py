import numpy as np
import random as rd
from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
def gen_image(arr, sz):
    two_d = (np.reshape(arr, (1, sz))*255//sz ).astype(np.uint8)
    # print(two_d)
    plt.imshow(two_d, interpolation='nearest',aspect='auto')
    return plt

def gen_inc_rand_array(len_of_array, no_of_arrays, randomness = 0.25):
	n1 = np.zeros((no_of_arrays, len_of_array))
	labels = np.zeros((1,no_of_arrays))
	no_of_changes = int(randomness*len_of_array)
	lower = 1
	upper = lower + len_of_array
	# print(n1,labels)
	for i in range(no_of_arrays):
		
		if rd.randrange(0,2) == 1:    # Increasing
			labels[0,i] = 1
			for k in range(len_of_array):
				n1[i][k] = lower + k
		else:
			for k in range(len_of_array-1,-1,-1): # decreasing
				# print("::::::",k,upper-k)
				n1[i][k] = upper-k
		
		for p in range(no_of_changes):
			n1[i][ rd.randrange(0,len_of_array) ] = rd.randrange(lower, upper)

	return n1, labels

def go(show_example):
	width_of_data = 14337
	no_of_rows = 100
	frc  = 0.8

	test_split = int(no_of_rows*frc)
	arrskew, arrLabels = gen_inc_rand_array(width_of_data,no_of_rows, 0.4)

	x_train, x_test = arrskew[0:test_split], arrskew[test_split:no_of_rows]

	y_train, y_test = arrLabels[0][0:test_split], arrLabels[0][test_split:no_of_rows]

	# print(arrskew, arrLabels, "\n", "."*50)
	# print(len(arrskew))
	# print("."*50)
	# print(x_train,"\n------------------\n",x_test)
	# print("---------------------\n",y_train,"\n------------------\n", y_test)



	clf = MLPClassifier()
	clf.fit(x_train, y_train)
	# print(clf)
	correct = 0
	total = 0
	done = True
	# k2 = 0
	for k in range( no_of_rows - test_split):
		predicted_ans = clf.predict([x_test[k]])
		real_ans = y_test[k]
		total +=1

		if predicted_ans == real_ans:
			correct+=1
		elif done :
			done = False
			# k2 = k
			if show_example:
				print("Test case",[x_test[k]])
				print("predicted_ans = ",predicted_ans)
				print("Real ans = ",real_ans)
				gen_image(x_test[k], width_of_data).show()
				
	print("Accuracy :",correct,"/",total," = ",correct*100/total)

		
go(True)  # Increasing is 1

