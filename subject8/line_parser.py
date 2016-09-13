import sys

from variable import Variable
from myplot import MyPlot

class Function(object):
    functions = {}
    def __init__(self):
        pass
    def CreateFunction(self, name):
        if name in Function.functions.keys():
            sys.exit('multiple definition for function ' + name + '!!!')
        else:
            Function.functions.update({name:{}})
            Function.functions[name].update({'operations':[]})
    def EndFunction(self, name):
        pass
    def CallFunction(self, name):
        for operation in Function.functions[name]['operations']:
            __parsed_line = LineParser(operation)
            __parsed_line.get_rule()
            __parsed_line.implement_rule()
    def AddToFunction(self, name, operation):
        if name in Function.functions.keys():
            Function.functions[name]['operations'].append(operation)
        else:
            sys.exit('no such function created ' + name + '!!!')

class LineParser(object):
    __rules = [
        'CREATEVAR',
        'SETVAR',
        'CALCULATE',
        'CREATEPLOT',
        'ADDTOPLOT',
        'SHOWPLOT',
        'CREATEFCT',
        'ENDFCT',
        'CALL']
    __function_create_start = None
    __variables = Variable()
    __plots = MyPlot()
    __functions = Function()

    def __init__(self, line):
        self.line = line
        self.error = 0
        self.rule_in_line = ''

    def update_globals(self, globals):
        pass
    def get_rule(self):
        for __rule in LineParser.__rules:
            __location = -1
            __matching_rules = 0
            while __matching_rules <=2: #search multiple identical rules in the same line
                __location = self.line.find(__rule, __location + 1)
                if __location == -1:
                    break
                else:
                    __matching_rules += 1
                    if __matching_rules == 1:
                        self.rule_in_line = __rule
                        self.error += 1
                    else:
                        self.error += 1
    def implement_rule(self):
        if LineParser.__function_create_start == None:
            if self.rule_in_line == 'CREATEVAR':
                LineParser.__variables.CreateVar((self.line.split(':')[1]).split('\n')[0])
                MyPlot.UpdateGlobals(Variable.variables)
            elif self.rule_in_line == 'SETVAR':
                LineParser.__variables.SetVar(self.line.split(':')[1], (self.line.split(':')[2]).split('\n')[0])
                MyPlot.UpdateGlobals(Variable.variables)
            elif self.rule_in_line == 'CALCULATE':
                LineParser.__variables.Calculate(self.line.split(':')[1], (self.line.split(':')[2]).split('\n')[0])
                MyPlot.UpdateGlobals(Variable.variables)
            elif self.rule_in_line == 'CREATEPLOT':
                LineParser.__plots.CreatePlot((self.line.split(':')[1]).split('\n')[0])
            elif self.rule_in_line == 'ADDTOPLOT':
                LineParser.__plots.AddToPlot(self.line.split(':')[1], self.line.split(':')[2], (self.line.split(':')[3]).split('\n')[0])
            elif self.rule_in_line == 'SHOWPLOT':
                LineParser.__plots.ShowPlot((self.line.split(':')[1]).split('\n')[0])
            elif self.rule_in_line == 'CREATEFCT':
                LineParser.__function_create_start = (self.line.split(':')[1]).split('\n')[0]
                LineParser.__functions.CreateFunction((self.line.split(':')[1]).split('\n')[0])
            elif self.rule_in_line == 'CALL':
                LineParser.__functions.CallFunction((self.line.split(':')[1]).split('\n')[0])
            else:
                pass
        else:
            if self.rule_in_line == 'CREATEVAR':
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'SETVAR':
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'CALCULATE':
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'CREATEPLOT':
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'ADDTOPLOT':
                LineParser.__functions = Function()
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'SHOWPLOT':
                LineParser.__functions.AddToFunction(LineParser.__function_create_start, self.line)
            elif self.rule_in_line == 'ENDFCT':
                LineParser.__function_create_start = None
