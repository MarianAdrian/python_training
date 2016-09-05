import sys

class Variable(object):
    variables = {}
    def CreateVar(self, name):
        if name in Variable.variables.keys():
            sys.exit('multiple definition for ' + name + '!!!')
        else:
            Variable.variables.update({name:''})
    def SetVar(self, name, value):
        print Variable.variables
        if name in Variable.variables.keys():
            Variable.variables[name]=value
        else:
            sys.exit('no such variable created ' + name + ' when setting variable!!!')
    def Calculate(self, dest_variable, function):
        if dest_variable in Variable.variables.keys():
            #to do
            pass
        else:
            sys.exit('no such variable created ' + name + ' when calculating expresion!!!')
