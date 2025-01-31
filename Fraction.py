class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        
        if isinstance(numerator, int):
            if isinstance(denominator, int):
                self.numerator = numerator
                self.denominator = denominator
            elif not isinstance(denominator, int):
                print("0")
            self.denominator = 1
        
        elif isinstance(numerator, str):
            numerator = numerator.strip().split('/')
            if len(numerator) == 2:
                try:
                    numerator, denominator = int(numerator[0]), int(numerator[1])
                    self.numerator, self.denominator = numerator, denominator
                except ValueError as e:
                    print("0")
            else:
                print("0")
            
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

if __name__ == "__main__":
    fraction = Fraction(5)
    print(fraction.get_denominator())