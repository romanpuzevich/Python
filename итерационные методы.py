import numpy as np

# матрица A
n = int(input("Число n системы:" ))
A = np.zeros(shape=(n+1, n+1))

A[0][0] = 1
for i in range(1, n):
    A[i][i-1] = 1
    A[i][i] = -2
    A[i][i+1] = 1

A[n][0] = 1
A[n][n] = 1
for i in range(1, n):
    A[n][i] = 2

# правая часть
f = np.zeros(n+1)
f[0] = 1
for i in range(1, n):
    f[i] = 2/(i+1)**2
f[n] = -n/3

print("Обусловленность матрицы А: ", np.linalg.cond(A))

# точное решение и печать невязки точного решения
x_ex = np.linalg.solve(A, f)
print("Точное решение:\n", x_ex, "\n")
print("Невязка точного решения:\n", A @ x_ex - f, "\n")
# погрешность точного решения находится в рамках машинной арифметики

# точность решения
tolerance = 10**(-6)
# начальное приближение
# k-тая инерация и k+1-ая итерцаия

x_k = np.zeros(n+1)
x_kp1 = np.empty(n+1)
# число итераций
iteration1 = 0


while np.linalg.norm(A @ x_kp1 - f) > tolerance:
    for i in range(0, n+1):
        x_kp1[i] = f[i]
        for j in range(0, i):
            x_kp1[i] = x_kp1[i] - A[i][j]*x_kp1[j]
        for j in range(i+1, n+1):
            x_kp1[i] = x_kp1[i] - A[i][j]*x_k[j]
        x_kp1[i] = x_kp1[i]/A[i][i]
    x_k[:] = x_kp1[:]
    iteration1 += 1

print("Решение методом Гаусса-Зейделя: \n", x_kp1, "\n")
print("Число итераций: ", iteration1, "\n")

y_k = np.zeros(n+1)
y_kp1 = np.empty(n+1)
iteration2 = 0

# метод Якоби
while np.linalg.norm(A @ y_kp1 - f) > tolerance:
    for i in range(0, n+1):
        y_kp1[i] = f[i]
        for j in range(0, i):
            y_kp1[i] = y_kp1[i] - A[i][j] * y_k[j]
        for j in range(i + 1, n + 1):
            y_kp1[i] = y_kp1[i] - A[i][j] * y_k[j]
        y_kp1[i] = y_kp1[i] / A[i][i]
    y_k[:] = y_kp1[:]
    iteration2 += 1

print("Решение методом Якоби: \n", y_kp1, "\n")
print("Число итераций: ", iteration2, "\n")


"""
D = np.zeros(shape=(n+1,n+1))
D[0][0] = 1
D[n][n] = 1
for i in range(1, n):
    D[i][i] = -2

B = np.linalg.inv(D)
C = D - A
print(C*B)

print(D)
print(A)
"""

"""
# метод простой итерации
w, v = np.linalg.eig(A)
tau = 2/(max(abs(w)) + min(abs(w)))

E = np.eye(n+1)
S = E - tau*A
b = tau*f

while np.linalg.norm(A @ x_kp1 - f) > tolerance:
    for i in range(0, n+1):
        x_kp1[i] = b[i]
        for j in range(0, n+1):
            x_kp1[i] = x_kp1[i] + S[i][j]*x_k[j]
    x_k[:] = x_kp1[:]
    iteration += 1

print(x_kp1)
"""