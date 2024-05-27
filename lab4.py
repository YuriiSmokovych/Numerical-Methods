# Лабораторна робота 4. Розв'язання систем лінійних рівнянь
import numpy as np
from scipy.linalg import solve

# Приклад матриці A і вектора b для розв'язку системи рівнянь Ax = b
A = np.array([[1, 2, -1], [3, 4, 1], [5, 1, -3]])
b = np.array([-3, 1, -2])

print("Матриця A:")
print(A)
print("Вектор b:")
print(b)

# Матричний метод
def matrix_method(A, b):
    A_inv = np.linalg.inv(A)
    return np.dot(A_inv, b)

# Метод Крамера
def cramer_method(A, b):
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "Система не має унікального розв'язку"
    n = A.shape[0]
    solutions = []
    for i in range(n):
        Ai = np.copy(A)
        Ai[:, i] = b
        solutions.append(np.linalg.det(Ai) / det_A)
    return solutions

# Метод Гауса
def gauss_method(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            if A[i, k] != 0.0:
                lam = A[i, k] / A[k, k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                b[i] = b[i] - lam * b[k]
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n])) / A[k, k]
    return x

def main():
    # Матричний метод
    X_matrix = matrix_method(A, b)
    print("Матричний метод:")
    print(X_matrix)

    # Метод Крамера
    X_cramer = cramer_method(A, b)
    print("Метод Крамера:")
    print(X_cramer)

    # Метод Гауса
    X_gauss = gauss_method(A.copy(), b.copy())  # Копіюємо, щоб уникнути зміни оригіналу
    print("Метод Гауса:")
    print(X_gauss)

    # Перевірка за допомогою функції solve з пакету scipy
    X_solve = solve(A, b)
    print("Перевірка за допомогою функції solve з пакету scipy:")
    print(X_solve)

if __name__ == "__main__":
    main()
