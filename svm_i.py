import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 

style.use('ggplot')

class SVM:
	def __init__(self, visualization = True):
		self.visualization = visualization
		self.colors = {1:'r',-1:'b'}
		if self.visualization:
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(1,1,1)
	def fit(self, data):  #train
		self.data = data
		print(self.data)
		# { |w| : [w,b]}
		optdict = {}
		transforms = [[1,1],[1,-1],[-1,-1],[-1,1]]
		all_data = []
		# yi is 1 or -1
		for yi in self.data:
			for featureset in self.data[yi]:
				for feature in featureset:
					all_data.append(feature)
		#alldata = [1, 7, 2, 8, 3, 8, 5, 1, 6, -1, 7, 3]
		print("alldata",all_data)
		self.max_feature_value = max(all_data)
		self.min_feature_value = min(all_data)
		print(self.max_feature_value,self.min_feature_value)  # 8 -1
		all_data = None

		step_sizes = [self.max_feature_value*0.1,
		self.max_feature_value*0.01,self.max_feature_value*0.001]
		b_range_multiple = 5
		b_multiple = 5
		latest_optimum = self.max_feature_value*10
		count=0
		for step in step_sizes:
			w = np.array([latest_optimum,latest_optimum])
			optimised = False
			while not optimised:
				for b in np.arange(-1*self.max_feature_value*b_range_multiple,self.max_feature_value*b_range_multiple, step*b_multiple):
					for transformation in transforms:
						w_t = w*transformation
						found_option = True
						for yi in self.data:
							for xi in self.data[yi]:
								
								if not yi*(np.dot(w_t, xi) + b)>=1:
									found_option = False
									# print('b',b,'w',w,'yi',yi,'xi',xi)
									count+=1
									break
						if found_option:
							optdict[np.linalg.norm(w_t)] = [w_t,b]
				if w[0]<0:
					optimised = True
					print("Optimised a step")
				else:
					w = w-step

			norms = sorted([n for n in optdict])
			opt_choice = optdict[norms[0]]
			print(optdict,"/"*15,opt_choice)
			self.w = opt_choice[0]
			self.b = opt_choice[1]
			latest_optimum = opt_choice[0][0]+step*2
		print("count ->",count,self.w,self.b)
			# print(optdict)

	def predict(self, features):
		# sign(x.w+b)
		# classification = sign
		classification = (np.sign(np.dot(np.array(features), self.w)+self.b))
		if(classification!=0 and self.visualization):
			self.ax.scatter(features[0],features[1],s=200,marker='*',c=self.colors[classification])

		return classification
	def visualize(self):
		[[self.ax.scatter(x[0],x[1],c=self.colors[i]) for x in datadict[i]] for i in datadict]
		def hyperplane(x,w,b,v):
			return (-w[0]*x-b+v) / w[1]
		datarange = (self.min_feature_value*0.9,self.max_feature_value*1.1)
		hyp_x_min = datarange[0]
		hyp_x_max = datarange[1]
		# positive support vector hyperplane
		psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
		psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
		self.ax.plot([hyp_x_min,hyp_x_max],[psv1,psv2],  'k')
		# negative support vector hyperplane
		nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
		nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
		self.ax.plot([hyp_x_min,hyp_x_max],[nsv1,nsv2],  'k')
		# decision boundary
		db1 = hyperplane(hyp_x_min, self.w, self.b, 0)
		db2 = hyperplane(hyp_x_max, self.w, self.b, 0)
		self.ax.plot([hyp_x_min,hyp_x_max],[db1,db2],  'y--')

		plt.show()

datadict= {-1:np.array([[1,7], [2,8],[3,8]]),
 1:np.array([[5,1],[6,-1],[7,3]])}

svm = SVM()
svm.fit(data = datadict)
svm.visualize()

# plt.scatter([ii[0] for i in datadict for ii in datadict[i]],
# 	[ii[1] for i in datadict for ii in datadict[i]])
# plt.show()