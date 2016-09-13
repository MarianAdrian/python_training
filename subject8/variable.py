import sys
from math import *

class Variable(object):
    variables = globals()
    def __init__(self):
        pass
    def CreateVar(self, name):
        if name in Variable.variables.keys():
            sys.exit('multiple definition for ' + name + '!!!')
        else:
            Variable.variables.update({name:''})
    def SetVar(self, name, value):
        if name in Variable.variables.keys():
            Variable.variables[name] = float(value)
        else:
            sys.exit('no such variable created ' + name + ' when setting variable!!!')
    def Calculate(self, dest_variable, function):
        if dest_variable in Variable.variables.keys():
            Variable.variables[dest_variable] = eval(function)
        else:
            sys.exit('no such variable created ' + name + ' when calculating expresion!!!')
