class Fraction(object):

    def __init__(self, numerator, denominator):

        if self.denominator == 0:
            raise ZeroDivisionError
        
        if isinstance(numerator,int):
            self.numerator = numerator
            self.denominator = 1
        elif isinstance(numerator,str):
            numerator = numerator.strip()
            split = numerator.split('/')
            numerator, denominator = int(split[0]), int(split[1])
            self.numerator, self.denominator = numerator, denominator

        if not isinstance(numerator,int) or not isinstance(denominator,int):
            raise TypeError

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