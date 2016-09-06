import sys
from math import sin

from variable import Variable
from myplot import MyPlot

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

__variables = None
__plots = None

def get_rule(line):
    error = 0
    rule_in_line = ''
    for rule in __rules:
        location = -1
        matching_rules = 0
        while matching_rules <=2: #search multiple identical rules in the same line
            location = line.find(rule, location + 1)
            if location == -1:
                break
            else:
                matching_rules += 1
                if matching_rules == 1:
                    rule_in_line = rule
                    error += 1
                else:
                    error += 1
    return error, rule_in_line

def implement_rule(line, rule):
    global __variables
    global __plots
    if rule == 'CREATEVAR':
        if __variables == None:
            __variables = Variable()
        __variables.CreateVar((line.split(':')[1]).split('\n')[0])
    elif rule == 'SETVAR':
        if __variables == None:
            __variables = Variable()
        __variables.SetVar(line.split(':')[1], (line.split(':')[2]).split('\n')[0])
    elif rule == 'CALCULATE':
        if __variables == None:
            __variables = Variable()
        __variables.Calculate(line.split(':')[1], (line.split(':')[2]).split('\n')[0])
    elif rule == 'CREATEPLOT':
        if __plots == None:
            __plots = MyPlot(__variables.Variable_globals)
        __plots.CreatePlot((line.split(':')[1]).split('\n')[0])
    elif rule == 'ADDTOPLOT':
        if __plots == None:
            __plots = MyPlot(__variables.Variable_globals)
        __plots.AddToPlot(line.split(':')[1], line.split(':')[2], (line.split(':')[3]).split('\n')[0])
    elif rule == 'SHOWPLOT':
        if __plots == None:
            __plots = MyPlot(__variables.Variable_globals)
        __plots.ShowPlot((line.split(':')[1]).split('\n')[0])

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        for index, line in enumerate(f.readlines()):
            err, rule = get_rule(line.split(';')[0]) #ignore comments on the line
            if err == 0:
                pass
            elif err == 1:
                implement_rule(line.split(';')[0], rule)
            else:
                sys.exit('line ' + str(index + 1) + ' from file ' + sys.argv[1] + ' has multiple commands !!!')
    
    #print Variable.variables