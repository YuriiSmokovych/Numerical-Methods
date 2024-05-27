import math

# 1. Визначити, яка рівність точніша
sqrt_14 = 3.74
div_49_13 = 49 / 13

error_sqrt_14 = abs(math.sqrt(14) - sqrt_14)
error_div_49_13 = abs(49 / 13 - 3.77)

if error_sqrt_14 < error_div_49_13:
    precise_equation = "14 ≈ 3.74"
else:
    precise_equation = "49 / 13 ≈ 3.77"

# 2. Визначити кількість правильних значущих цифр наближеного числа
narrow_approx = 5.6483
narrow_error = 0.0017
broad_approx = 83.736
broad_error = broad_approx * 0.00085

# 3. Знайти граничні абсолютні та відносні похибки чисел
narrow_limit_error = narrow_error
broad_limit_error = broad_error

# Виведення результатів
print(f"1. Точніша рівність: {precise_equation}")
print(f"2. Кількість правильних значущих цифр:")
print(f"   а) У вузькому розумінні: {narrow_approx} ± {narrow_error}")
print(f"   б) У широкому розумінні: {broad_approx}; δ = 0.085%")
print(f"3. Граничні абсолютні та відносні похибки:")
print(f"   а) У вузькому розумінні: {narrow_limit_error}")
print(f"   б) У широкому розумінні: {broad_limit_error}")
