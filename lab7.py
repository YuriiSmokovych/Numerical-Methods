import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390])
yi = np.array([4.2556, 4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706])
x_values = [1.361,1.346,1.342,1.394,1.381,1.386]

def calculate_differences(y_values):
    differences = [y_values]
    n = len(y_values)
    for i in range(1, n):
        differences.append(np.diff(differences[-1]))
    return differences
def newton_coefficients(xi, yi):
    differences = calculate_differences(yi)
    coefficients = [differences[0][0]]
    n = len(xi)
    for i in range(1, n):
        coefficients.append(differences[i][0] / np.math.factorial(i))
    return coefficients
def interpolate_newton_polynomial(xi, coefficients, x_values):
    result = []
    for x in x_values:
        y = coefficients[0]
        for i in range(1, len(coefficients)):
            term = coefficients[i]
            for j in range(i):
                term *= (x - xi[j])
            y += term
        result.append(y)
    return result

coefficients = newton_coefficients(xi, yi)
interpolated_values = interpolate_newton_polynomial(xi, coefficients, x_values)

plt.figure(figsize=(10, 6))
plt.plot(xi, yi, 'bo', label='Дані')
plt.plot(x_values, interpolated_values, 'r-', label='Інтерполяційна функція')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Інтерполяція функції за допомогою багаточлена Ньютона')
plt.legend()
plt.grid(True)
plt.show()