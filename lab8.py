import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
x = np.array([1.1, 1.4, 1.9, 2.5, 2.7])
y = np.array([2.91, 3.64, 4.55, 2.57, 0.24])
cs = CubicSpline(x, y)
y_cs = cs(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Вузли')
plt.plot(x, y_cs, label='Сплайн')
plt.title('Графік кубічного сплайну')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()