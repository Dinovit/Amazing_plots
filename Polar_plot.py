import pylab
import numpy as np

r = np.arange(0, 1, 0.01)
theta = 4 * np.pi * r

pylab.axes(projection='polar')
pylab.plot(theta,r,'o')
