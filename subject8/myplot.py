import sys
#from matplotlib import *
from math import *

import numpy as np
import matplotlib.pyplot as plt

class MyPlot(object):
    MyPlot_globals = {}
    def __init__(self):
        pass
    def CreatePlot(self, plot_name):
        if plot_name in MyPlot.MyPlot_globals:
            sys.exit('multiple plot definition for ' + name + '!!!')
        else:
            MyPlot.MyPlot_globals.update({plot_name:{'MyPlot':plt, 'x_values':[], 'y_values':[]}})
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
            MyPlot.MyPlot_globals[plot_name]['x_values'].append(x)
            MyPlot.MyPlot_globals[plot_name]['y_values'].append(y)
        else:
            sys.exit('no such plot created ' + name + ' when adding to plot!!!')
    def ShowPlot(self, plot_name):
        MyPlot.MyPlot_globals[plot_name]['MyPlot'].axis([min(MyPlot.MyPlot_globals[plot_name]['x_values'])-2,
                                                         max(MyPlot.MyPlot_globals[plot_name]['x_values'])+2,
                                                         min(MyPlot.MyPlot_globals[plot_name]['y_values'])-2,
                                                         max(MyPlot.MyPlot_globals[plot_name]['y_values'])+2])
        MyPlot.MyPlot_globals[plot_name]['MyPlot'].ylabel('Y')
        MyPlot.MyPlot_globals[plot_name]['MyPlot'].xlabel('X')
        MyPlot.MyPlot_globals[plot_name]['MyPlot'].plot(MyPlot.MyPlot_globals[plot_name]['x_values'], MyPlot.MyPlot_globals[plot_name]['y_values'])
        MyPlot.MyPlot_globals[plot_name]['MyPlot'].show()
    @staticmethod
    def UpdateGlobals(globals):
        MyPlot.MyPlot_globals.update(globals)
