import sys
from math import *

class Variable(object):
    variables = {}
    def __init__(self):
        self.Variable_globals = globals()
    def CreateVar(self, name):
        if name in Variable.variables.keys():
            sys.exit('multiple definition for ' + name + '!!!')
        else:
            Variable.variables.update({name:''})
            self.Variable_globals[name] = ''
    def SetVar(self, name, value):
        if name in Variable.variables.keys():
            Variable.variables[name]=value
            self.Variable_globals[name] = float(value)
        else:
            sys.exit('no such variable created ' + name + ' when setting variable!!!')
    def Calculate(self, dest_variable, function):
        if dest_variable in Variable.variables.keys():
            Variable.variables[dest_variable] = eval(function)
            self.Variable_globals[dest_variable] = Variable.variables[dest_variable]
        else:
            sys.exit('no such variable created ' + name + ' when calculating expresion!!!')
