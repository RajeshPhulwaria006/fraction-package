from math import gcd
class Fraction:
    def __init__(self, num, den):
        if den == 0:    raise ZeroDivisionError("Denomenator cannot be Zero!")
        if den < 0:
            num = -num
            den = -den

        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
    
    # basic operations
    def __add__(self, other):
        other = self._convert(other)
        if other is NotImplemented:
            return NotImplemented
            
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
        
    def __sub__(self, other):
        other = self._convert(other)
        if other is NotImplemented:
            return NotImplemented
        
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __mul__(self, other):
        other = self._convert(other)
        if other is NotImplemented:
            return NotImplemented
        
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
    
    def __truediv__(self, other):
        other = self._convert(other)
        if other is NotImplemented:
            return NotImplemented
            
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)
    
    # comparision operations
    def __eq__(self, other):
        return (self.num/other.den) == (self.num/other.den)

    def __gt__(self, other):
        return (self.num/other.den) > (self.num/other.den)

    def __lt__(self, other):
        return (self.num/other.den) < (self.num/other.den)

    def __le__(self, other):
        return (self.num/other.den) <= (self.num/other.den)

    def __ge__(self, other):
        return (self.num/other.den) >= (self.num/other.den)
    
    # undary operations
    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __pos__(self):
        return Fraction(self.num, self.den)

    def __abs__(self):
        return Fraction(abs(self.num), self.den)

    # type convergence
    def __int__(self):
        return int(self.num / self.den)
    
    def __float__(self):
        return self.num / self.den
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __bool__(self):
        return self.num != 0
    
    def _convert(self, other):
        if isinstance(other, Fraction):
            return other
        elif isinstance(other, int):
            return Fraction(other, 1)
        return NotImplemented
    
    # right hand operands
    def __radd__(self, other):
        return self + other
    def __rmul__(self, other):
        return self * other
    # to maintain order
    def __rsub__(self, other):
        other = self._convert(other)
        return other - self
    def __rtruediv__(self, other):
        other = self._convert(other)
        return other / self