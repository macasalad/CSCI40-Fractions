class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        
        if isinstance(numerator, float): 
            self.numerator, self.denominator = 0, 1

        elif isinstance(numerator, int):
            if isinstance(denominator, int):
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
                except ValueError:
                    self.numerator, self.denominator = 0, 1
            elif len(numerator) == 1:
                try:
                    numerator = int(numerator[0])
                    self.numerator, self.denominator = numerator, 1
                except ValueError:
                    self.numerator, self.denominator = 0, 1
            else:
                self.numerator, self.denominator = 0, 1

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