# Example 1: Floating point addition problem
a = 0.1 + 0.2
print("0.1 + 0.2 =", a)

# Example 2: Very close numbers
b = 1.0000001
c = 1.0000002
print("b - c =", b - c)

# Solution 1: Using Decimal module
from decimal import Decimal

a_decimal = Decimal('0.1') + Decimal('0.2')
print("Using Decimal: 0.1 + 0.2 =", a_decimal)
