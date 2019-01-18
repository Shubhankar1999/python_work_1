

import numpy as np 
from matplotlib import pyplot

y = 15
y2 = y**2
x = np.zeros(y2)
for i in range(y2):
	x[i] = i

toplot = (np.reshape(x, ( y, y) )).astype(np.uint8)
pyplot.imshow(toplot)
pyplot.show()