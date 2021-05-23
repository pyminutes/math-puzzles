# Symbolic mathematics
import sympy as sym

# Define symbolic variables and equations
x, y = sym.symbols('x, y')
eq_1 = x**2 - 17*x - y
eq_2 = y**2 - x - 17*y

# Solve the equations
solution = sym.solve((eq_1, eq_2), (x, y))

# Display solutions where x is not equal to y
for x, y in solution:
    if x != y:
        z = sym.sqrt(x**2 + y**2 + 1)
        print(f'z = {sym.simplify(z)}')
