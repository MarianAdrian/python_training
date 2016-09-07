import sys
from math import sin

from line_parser import LineParser

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        for index, line in enumerate(f.readlines()):
            parse_line = LineParser(line.split(';')[0])
            parse_line.get_rule()
            if parse_line.error == 0:
                pass
            elif parse_line.error == 1:
                parse_line.implement_rule()
            else:
                sys.exit('line ' + str(index + 1) + ' from file ' + sys.argv[1] + ' has multiple commands !!!')
