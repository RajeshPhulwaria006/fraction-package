from fractions import Fraction

def test_add():
    assert Fraction(1,2) + Fraction(1,2) == Fraction(1,1)

def test_sub():
    assert Fraction(3,2) - Fraction(1,2) == Fraction(1,1)

def test_mul():
    assert Fraction(2,3) * Fraction(3,4) == Fraction(1,2)

def test_div():
    assert Fraction(1,2) / Fraction(3,4) == Fraction(2,3)

def test_reduce():
    assert Fraction(2,4) == Fraction(1,2)