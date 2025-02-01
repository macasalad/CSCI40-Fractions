class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        
        # Checks the validity of the input
        if isinstance(numerator, float):
            self.numerator, self.denominator = 0, 1

        elif isinstance(numerator, int):
            if isinstance(denominator, int): # Checks the validity of the denominator
                self.numerator, self.denominator = numerator, denominator
            else:
                self.numerator, self.denominator = 0, 1
        
        elif isinstance(numerator, str):
            numerator = numerator.strip().split('/')
            if len(numerator) == 2:
                try:
                    numerator, denominator = int(numerator[0]), int(numerator[1])
                    if denominator == 0:
                        raise ZeroDivisionError
                    else:
                        self.numerator, self.denominator = numerator, denominator
                except ValueError: # If the inputs are not integers
                    self.numerator, self.denominator = 0, 1
            elif len(numerator) == 1:
                try:
                    numerator = int(numerator[0])
                    self.numerator, self.denominator = numerator, 1
                except ValueError: # If the input is not an integer
                    self.numerator, self.denominator = 0, 1
            else: # If there are more than 2 inputs
                self.numerator, self.denominator = 0, 1

    def gcd(a, b):
        '''
        Returns the greatest common divisor of 2 integers a and b
        '''
        if a == 0 or b == 0:
            return 0
        
        # Implements the Euclidian algorithm
        while b:
            a, b = b, a%b
        
        return abs(a)

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass