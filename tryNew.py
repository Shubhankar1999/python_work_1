import numpy as np
import random as rd

def generate_skewed_arrays(len_of_array, no_of_arrays, prob_of_one = 0.75, inv_degree_of_rand = 50):
	err = False
	if inv_degree_of_rand <1 or inv_degree_of_rand >200:
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
	labels = np.zeros(no_of_arrays)
	dor2 = inv_degree_of_rand+0.5
	for k in range(no_of_arrays):
		right_skewed = True
		if rd.randrange(0,2)==1:
			right_skewed = False
		if not right_skewed:
			labels[k] = 1

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

arrskew, arrLabels = generate_skewed_arrays(14,100,0.75, 110)
for i in range(10):
	print(arrskew[i]," "*3,arrLabels[i])


