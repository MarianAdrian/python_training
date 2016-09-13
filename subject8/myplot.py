import sys
#from matplotlib import *
from math import *

import numpy as np
import matplotlib.pyplot as plt

class MyPlot(object):
    MyPlot_globals = {}
    def __init__(self):
        #self.MyPlot_globals = globals
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
        pass
    def CreatePlot(self, plot_name):
        if plot_name in MyPlot.MyPlot_globals:
            sys.exit('multiple plot definition for ' + name + '!!!')
        else:
            MyPlot.MyPlot_globals.update({plot_name:plt})
    def AddToPlot(self, plot_name, plot_x, plot_y):
        if plot_name in MyPlot.MyPlot_globals:
            if plot_x in MyPlot.MyPlot_globals.keys():
                x = MyPlot.MyPlot_globals[plot_x]
            else:
                x = float(plot_x)
            if plot_y in MyPlot.MyPlot_globals.keys():
                y = MyPlot.MyPlot_globals[plot_y]
            else:
                y = float(plot_y)
            x = np.arange(-10, 10, 0.1)
            #x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
            MyPlot.MyPlot_globals[plot_name].plot(x, -x+2)
            #print 'y=' + str(y)
            MyPlot.MyPlot_globals[plot_name].plot(x, x**6)
        else:
            sys.exit('no such plot created ' + name + ' when adding to plot!!!')
    def ShowPlot(self, plot_name):
        MyPlot.MyPlot_globals[plot_name].axis([-10.0, 10.0, -10.0, 10.0])
        MyPlot.MyPlot_globals[plot_name].ylabel('Y')
        MyPlot.MyPlot_globals[plot_name].xlabel('X')
        MyPlot.MyPlot_globals[plot_name].show()
    @staticmethod
    def UpdateGlobals(globals):
        MyPlot.MyPlot_globals.update(globals)
