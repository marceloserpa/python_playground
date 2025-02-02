import matplotlib.pyplot as plt
import numpy
 
datapoints = numpy.array([[9, 1, 2, 7, 5, 8, 3, 4, 6],
                 [4, 2, 3, 7, 9, 1, 6, 5, 8]])
 
categories = numpy.array([0, 1, 1, 0, 1, 0, 0, 1, 1])
 
colormap = numpy.array(['r', 'b'])
 
plt.scatter(datapoints[0], datapoints[1], s=100, c=colormap[categories])
plt.show()