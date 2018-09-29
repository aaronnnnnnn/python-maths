import math
from getInput import getInput

class Quadratic():
    def __init__(self, xSquared=None, x=None, number=None, precision=None):
        self.quadratic = [1.0, 10.0, 1.0]
        self.results = [0.0, 0.0]
        self.equation = ''

        if xSquared is not None:
            self.quadratic[0] = xSquared

        if x is not None:
            self.quadratic[1] = x

        if number is not None:
            self.quadratic[2] = number

        if precision is None:
            self.precision = 3
        else:
            self.precision = precision

    #Solves the quadratic using the quadratic equation
    def calculateQuadratic(self):
        # Isolate numbers from array
        a, b, c = self.quadratic
        try:
            xSign, nSign = '+', '+'
            if b < 0:
                xSign = ''
            
            if c < 0:
                nSign = ''  # Decide on signs for displaying it

            self.equation = '%sx²%s%sx%s%s' % (a, xSign, b, nSign, c)

            
            # Work out a bit of the top half of the equation
            sqrt = math.sqrt(((b*b) - (4.0*a*c)))
            bottom = 2.0 * a  # Work out bottom half of equation

            # Plus side
            top = -b + sqrt  # Finish top side
            self.results[0] = (top/bottom)  # Find one solution

            # Minus side
            top = -b - sqrt  # Also finish top side
            self.results[1] = (top/bottom)  # Find other solution

            self.results[0], self.results[1] = round(self.results[0], self.precision), round(self.results[1], self.precision)
        except:
            print('The quadratic is not solvable')

    def getQuadratic(self):
        return self.results

    def getEquation(self):
        return self.equation




    #Gets the three terms of the quadratic, either from input, or from arguments
    # def getQuadratic(self):
    #     if self.xSquared == 'no' and self.x == 'no' and self.number == 'no':
    #         while True:  # Loop through until quadratic is correct
    #             xSquared = getInput('What is the coefficient of x²', 'float')
    #             x = getInput('What is the coefficient of x', 'float')
    #             number = getInput('What is the coefficient of the number', 'float')  #Get three coeffecients

    #             xSign, nSign = '+', '+'
    #             if x < 0:
    #                 xSign = ''
                
    #             if number < 0:
    #                 nSign = ''  # Decide on signs for displaying it

    #             self.equation = '%sx²%s%sx%s%s' % (xSquared, xSign, x, nSign, number)
    #             questionAsk = 'Is %s your quadratic' % (self.equation)
    #             # Ask if the quadratic is correct
    #             question = getInput(questionAsk, 'str')
    #             if question.upper() == 'YES' or question.upper() == 'Y':
    #                 # Return the coefficients
    #                 self.quadratic = [xSquared, x, number]
    #                 break
    #             else:
    #                 print('Input again')  # Start again
    #     else:
    #         xSign = '+'
    #         if self.x < 0:
    #             xSign = ''

    #         nSign = '+'
    #         if self.number < 0:
    #             nSign = ''  # Decide on signs for displaying it

    #         self.equation = '%sx²%s%sx%s%s' % (self.xSquared, xSign, self.x, nSign, self.number)
    #         self.quadratic = [self.xSquared, self.x, self.number]


