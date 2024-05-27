import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Задані значення x
x = np.linspace(0, 1, 10)

# Функція f(x) = e^(-x) + x^2
def func(x):
    return np.exp(-x) + x**2

# Обчислення значень y
y = func(x)

# Друк значень
print('x =', x)
print('y =', y)

# Апроксимація прямою
def linear_func(a, x, y):
    return a[0] + a[1] * x - y

a0 = np.array([1, 1])
res_lsq_linear = least_squares(linear_func, x0=a0, args=(x, y))
print("a0 = %.2f, a1 = %.2f" % tuple(res_lsq_linear.x))

x_p = np.linspace(min(x), max(x), 100)
y_p_linear = res_lsq_linear.x[0] + res_lsq_linear.x[1] * x_p

plt.plot(x, y, 'o', label='Вихідні точки')
plt.plot(x_p, y_p_linear, 'r', label='Апроксимація прямою')
plt.title("Метод найменших квадратів - Пряма")
plt.legend()
plt.grid(True)
plt.show()

# Апроксимація параболою
def parabolic_func(a, x, y):
    return a[0] + a[1] * x + a[2] * x**2 - y

a0 = np.array([1, 1, 1])
res_lsq_parabolic = least_squares(parabolic_func, x0=a0, args=(x, y))
print("a0 = %.2f, a1 = %.2f, a2 = %.2f" % tuple(res_lsq_parabolic.x))

y_p_parabolic = res_lsq_parabolic.x[0] + res_lsq_parabolic.x[1] * x_p + res_lsq_parabolic.x[2] * x_p**2

plt.plot(x, y, 'o', label='Вихідні точки')
plt.plot(x_p, y_p_parabolic, 'b', label='Апроксимація параболою')
plt.title("Метод найменших квадратів - Парабола")
plt.legend()
plt.grid(True)
plt.show()
