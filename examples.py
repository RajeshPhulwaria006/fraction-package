from fractions import Fraction

num1 = Fraction(4, 5)
num2 = Fraction(3, 2)

# print(type(num1))
print("addition: ", num1 + num2)
print("subtraction: ", num1 - num2)
print("multiplication: ", num1 * num2)
print("division: ", num1 / num2)

print("Integer convergence: ", int(num1))
print("Float convergence: ", float(num1))

# x = Fraction(1, 0)
x = Fraction(5, 2)
print(5 + x)
print(isinstance(x, Fraction))