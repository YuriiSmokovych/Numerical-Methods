import numpy as np
import matplotlib.pyplot as plt
x_values = np.array([-4, -2, 0, 3])
f_values = np.array([-18, 8, -6, 3])
xi_values = np.array([-3.5, -3, -0.5, 2])
def lagrange_interpolation(x, x_values, f_values):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = f_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result
f_approx = lagrange_interpolation(xi_values, x_values, f_values)
plt.figure(figsize=(9, 7))
plt.plot(x_values, f_values, 'bo', label='Вихідні точки')
plt.plot(xi_values, f_approx, 'r+', label='Наближені значення')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Інтерполяційний багаточлен Лангранжа')
plt.legend()
plt.grid(True)
plt.show()
print("Наближені значення f(xi):", f_approx)