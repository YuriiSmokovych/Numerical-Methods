import numpy as np
import numdifftools as nd

# Визначаємо нову функцію
def f(x):
    return np.sin(x) - 0.5 * x

# Метод Ньютона (метод дотичних)
def newton_method(a, b, eps, f):
    df2 = nd.Derivative(f, n=2)(b)
    if f(b) * df2 > 0:
        xi = b
    else:
        xi = a
    df = nd.Derivative(f, n=1)(xi)
    xi_1 = xi - f(xi) / df
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - f(xi) / df
    return xi_1

# Комбінований метод
def combined_method(a, b, eps, f):
    if nd.Derivative(f, n=1)(a) * nd.Derivative(f, n=2)(a) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai - bi) > eps:
        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
        bi_1 = bi - f(bi) / nd.Derivative(f, n=1)(bi)
        ai = ai_1
        bi = bi_1
    return (ai_1 + bi_1) / 2

# Параметри
a1, b1 = 0, 2
a2, b2 = 2, 4
eps = 0.001

# Знаходимо корені
root_newton_1 = newton_method(a1, b1, eps, f)
root_combined_1 = combined_method(a1, b1, eps, f)

root_newton_2 = newton_method(a2, b2, eps, f)
root_combined_2 = combined_method(a2, b2, eps, f)

# Виведення результатів
print(f"Корінь на відрізку [0, 2] (метод Ньютона): {root_newton_1:.5f}")
print(f"Корінь на відрізку [0, 2] (комбінований метод): {root_combined_1:.5f}")

print(f"Корінь на відрізку [2, 4] (метод Ньютона): {root_newton_2:.5f}")
print(f"Корінь на відрізку [2, 4] (комбінований метод): {root_combined_2:.5f}")
