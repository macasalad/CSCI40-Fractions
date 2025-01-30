class Fraction(object):

    def __init__(self, numerator, denominator):

        if isinstance(numerator,int):
            self.numerator = numerator
            self.denominator = 1

        #elif isinstance(numerator,str):
        #elif isinstance(numerator,float):

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
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