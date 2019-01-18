from statistics import mean
import numpy as np 
import random
import matplotlib.pyplot as plt
from matplotlib import style 
style.use('fivethirtyeight')

#xs = np.array([1,2,3,4,5,6],dtype = np.float64)
#ys = np.array([5,4,6,5,6,7], dtype = np.float64)
#print(1+2+3+4+5+6+7+8)
def create_dataset(howMuch, var, step=2, correlation = False):
	hm = howMuch
	val  =1
	ys = []
	for i in range(hm):

		y = val + random.randrange(-var,var)
		ys.append(y)
		if correlation and correlation == 'pos':
			val+=step
		elif correlation and correlation == 'neg':
			val-=step
	xs = [i for i in range (len(ys))]

	return np.array(xs,dtype = np.float64), np.array(ys, dtype = np.float64)

def best_fit_slope(xs,ys):

	m = (mean(xs)*mean(ys) - mean(xs*ys))/((mean(xs)**2 - mean(xs**2)))
	b = mean(ys) - m*mean(xs)
	return m,b
def sq_error(ys_o,y_l):

	return sum((y_l - ys_o)**2) 

def coeff_of_det(ys_o,ys_l):
	y_mean = mean(ys_l)
	sq_error_regrr = sq_error(ys_o,ys_l)
	sq_error_y_mean = sq_error(ys_o,y_mean)
	r2 = 1 - (sq_error_regrr/sq_error_y_mean)
	return r2

xs,ys = create_dataset(40,10,2,correlation='pos')
print(xs,"\n",ys)
m,b = best_fit_slope(xs,ys)

guesses = [(m*x)+b for x in xs]
#print(guesses)
r_sq = coeff_of_det(ys,guesses)
print(m,b," Error : ",r_sq)

plt.scatter(xs,ys)

plt.plot(xs,guesses)
plt.show()