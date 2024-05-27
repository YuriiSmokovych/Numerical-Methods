import numpy as np
from scipy.misc import derivative

def f(x):
    return 9*x**4 + 8*x**3 + 1.5*x**2 + 2*x - 10

def bisection_method(a, b, eps):
    while (b - a) / 2.0 > eps:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def chord_method(a, b, eps):
    if f(a) * derivative(f, a, n=2) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    
    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    return xi_1

# Знаходимо корені методом половинного ділення
a, b = 0, 1
root_bisection = bisection_method(a, b, 0.0001)
print(f"Корінь (метод половинного ділення): {root_bisection:.5f}")

# Знаходимо корені методом хорд
root_chord = chord_method(a, b, 0.0001)
print(f"Корінь (метод хорд): {root_chord:.5f}")
