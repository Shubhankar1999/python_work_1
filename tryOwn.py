import numpy as np
import random as rd
from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
def gen_image(arr, sz):
    two_d = (np.reshape(arr, (1, sz)) ).astype(np.uint8)
    plt.imshow(two_d, interpolation='nearest')
    return plt

def generate_skewed_arrays(len_of_array, no_of_arrays, prob_of_one = 0.75, inv_degree_of_rand = 10):
	err = False
	if inv_degree_of_rand <1 or inv_degree_of_rand >100:
		print("ERROR -> inv_degree_of_rand")
		err = True
	if len_of_array<2:
		print("ERROR -> len_of_array")
		err = True
	if no_of_arrays<1:
		print("ERROR -> no_of_arrays")
		err = True
	if prob_of_one<0 or prob_of_one>1:
		print("ERROR -> prob_of_one")
		err = True
	if err:
		return
	n1 = np.zeros((no_of_arrays ,len_of_array))
	labels = np.zeros((1,no_of_arrays))
	dor2 = inv_degree_of_rand+0.5
	for k in range(no_of_arrays):
		right_skewed = True
		if rd.randrange(0,2)==1:
			right_skewed = False
		if not right_skewed:
			labels[0,k] = 1

			for i in range(int(prob_of_one*len_of_array)):
				r1 = rd.randrange(0, int(dor2*len_of_array))
				if (r1 < inv_degree_of_rand*len_of_array):
					r1 = r1//(inv_degree_of_rand*2)
				else:
					r1 = int(r1 - (inv_degree_of_rand-0.5)*len_of_array)
				n1[k][r1] = 1
		else:
			for i in range(int(prob_of_one*len_of_array)):
				r1 = rd.randrange(0, int(dor2*len_of_array))
				if (r1 < inv_degree_of_rand*len_of_array):
					r1 = int(r1/(inv_degree_of_rand*2) + len_of_array/2)
				else:
					r1 = r1 - inv_degree_of_rand*len_of_array

				n1[k][r1] = 1


	return n1, labels

def go(show_example):
	width_of_data = 36
	no_of_rows = 100
	frc  = 0.8

	test_split = int(no_of_rows*frc)
	arrskew, arrLabels = generate_skewed_arrays(width_of_data,no_of_rows,0.75, 1)

	x_train, x_test = arrskew[0:test_split], arrskew[test_split:no_of_rows]

	y_train, y_test = arrLabels[0][0:test_split], arrLabels[0][test_split:no_of_rows]

	# print(arrskew, arrLabels, "\n", "."*50)
	# print(len(arrskew))
	# print("."*50)
	# print(x_train,"\n------------------\n",x_test)
	# print("---------------------\n",y_train,"\n------------------\n", y_test)



	clf = MLPClassifier()
	clf.fit(x_train, y_train)

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
		if correct == total-1 and done:
			done = False
			# k2 = k
			if show_example:
				gen_image(x_test[k2], width_of_data).show()
				print("Test case",[x_test[k]])
				print("predicted_ans = ",predicted_ans)
				print("Real ans = ",real_ans)
			
	print(correct*100/total)
	
		

go(True)