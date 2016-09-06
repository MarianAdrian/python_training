import sys
#from matplotlib import *

import numpy as np
import matplotlib.pyplot as plt

class MyPlot(object):
    plots = []
    def __init__(self):
        X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        C, S = np.cos(X), np.sin(X)

        plt.plot(X, C)
        plt.plot(X, S)

        plt.show()
    def CreatePlot(self, plot_name):
        pass
    def AddToPlot(self, plot_name, plot_x, plot_y):
        pass
    def ShowPlot(self, plot_name):
        pass
