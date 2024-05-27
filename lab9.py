import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial
import sympy as sp

# Визначення функції
def f(x):
    return np.exp(-2*x) + x**2

# Символьна змінна
x = sp.symbols('x')
f_sym = sp.exp(-2*x) + x**2

# Похідні
f1 = sp.diff(f_sym, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)

# Значення в точці x = 0
x0 = 0
f_x0 = f_sym.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Поліном Тейлора
T = f_x0 + f1_x0*(x-x0) + (f2_x0/2)*(x-x0)**2 + (f3_x0/6)*(x-x0)**3

# Виведення значень
print("f(0) =", f_x0)
print("T(x) =", T)

# Побудова графіків
x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f(xi) for xi in x_vals])
T_vals = np.array([T.subs(x, xi).evalf() for xi in x_vals])

plt.plot(x_vals, f_vals, label="f(x)")
plt.plot(x_vals, T_vals, label="T(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення многочленом Тейлора")
plt.grid(True)
plt.show()

# Побудова багаточлена Тейлора за допомогою scipy.interpolate.approximate_taylor_polynomial
taylor = approximate_taylor_polynomial(f, 0, 3, 1)
print('taylor =', taylor)

plt.plot(x_vals, f(x_vals), label="f(x)", color='blue')
plt.plot(x_vals, taylor(x_vals), label=f"degree=3", color='red', linestyle='--')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення багаточленами Тейлора")
plt.grid()
plt.show()
