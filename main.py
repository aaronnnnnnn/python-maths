"""
Python Quadratic Solver - Solves a quadratic formula using the quadratic equation

"""

import argparse
import quadratic




class args:
    coeffecients = None
    precision = None


parser = argparse.ArgumentParser(description='Solve a quadratic')
parser.add_argument('-c', dest='coeffecients', type=float, nargs=3)
parser.add_argument('-p', dest='precision', type=int)
args = parser.parse_args()


if args.coeffecients is not None and args.precision is not None:
    quadratic = quadratic.Quadratic(
        args.coeffecients[0], args.coeffecients[1], args.coeffecients[2], args.precision)
elif args.coeffecients is not None:
    quadratic = quadratic.Quadratic(
        args.coeffecients[0], args.coeffecients[1], args.coeffecients[2])
elif args.precision is not None:
    quadratic = quadratic.Quadratic(args.precision)
else:
    quadratic = quadratic.Quadratic()

quadratic.calculateQuadratic()

def printQuadratic():
    results = quadratic.getQuadratic()
    print('For the equation:', quadratic.getEquation())
    print('X = %s or %s' % (results[0], results[1])) 



printQuadratic()
