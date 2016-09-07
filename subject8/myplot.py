import sys
#from matplotlib import *

import numpy as np
import matplotlib.pyplot as plt

class MyPlot(object):
    plots = []
    plot_globals = None
    def __init__(self, globals):
        self.MyPlot_globals = globals
        #print self.MyPlot_globals.keys()
        #X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        #C, S = np.cos(X), np.sin(X)
        #
        #test = plt
        #
        #test.plot(X, C)
        #test.plot(X, S)
        #
        #
        #
        #test.show()
        #plt.show()
    def CreatePlot(self, plot_name):
        if plot_name in MyPlot.plots:
            sys.exit('multiple plot definition for ' + name + '!!!')
        else:
            MyPlot.plots.append(plot_name)
            self.MyPlot_globals[plot_name] = plt
    def AddToPlot(self, plot_name, plot_x, plot_y):
        if plot_name in MyPlot.plots:
            if plot_x in self.MyPlot_globals.keys():
                x = self.MyPlot_globals[plot_x]
            else:
                x = float(plot_x)
            if plot_y in self.MyPlot_globals.keys():
                y = self.MyPlot_globals[plot_y]
            else:
                y = float(plot_y)
            self.MyPlot_globals[plot_name].plot(x, y)
        else:
            sys.exit('no such plot created ' + name + ' when adding to plot!!!')
    def ShowPlot(self, plot_name):
        #self.MyPlot_globals[plot_name].xlim(-4.0, 4.0)
        self.MyPlot_globals[plot_name].show()
