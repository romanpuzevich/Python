import numpy as np


def var(n):
    def size(n):
        return int(1/n+1)

    x = np.zeros(size(n))
    for i in range(1,size(n)):
        x[i] = x[i-1]+n
    return x, size(n)


def function(x):
    return np.e**x


def rect(n):
    n1 = n
    x, size = var(n1)
    integral = float(0)
    for i in range(1, size):
        integral += function(x[i-1] + n/2)*(x[i] - x[i-1])
    return integral


def trap(n):
    n1 = n
    x, size = var(n1)
    integral = float(0)
    for i in range(1, size):
        integral += (function(x[i])+function(x[i-1]))*(x[i] - x[i-1]) / 2
    return integral


def simp(n):
    n1 = n
    x, size = var(n1)
    integral = float(0)
    for i in range(1, size):
        integral += (function(x[i]) + 4*function(x[i - 1]+n/2) + function(x[i - 1])) * (x[i] - x[i - 1]) / 6
    return integral

def runge(func, half_step, step):
    if func == 'rect':
        return (half_step - step) / (2 - 1)
    elif func == 'trap':
        return (half_step - step) / (2**2 - 1)
    elif func == 'simp':
        return (half_step - step) / (2**4 - 1)


print('Значение методом прямоугольников: ', rect(0.01), '\n',
      'Погрешность методом Рунге:', runge('trap', rect(0.01), rect(0.02)), '\n',
      'Реальная погрешность: ', rect(0.01) - (np.exp(1) - 1), '\n')

print('Значение методом трапеций: ', trap(0.01), '\n',
      'Погрешность методом Рунге:', runge('trap', trap(0.01), trap(0.02)), '\n',
      'Реальная погрешность: ', trap(0.01) - (np.exp(1) - 1), '\n')

print('Значение методом Симпсона: ', simp(0.01), '\n',
      'Погрешность методом Рунге:', runge('trap', simp(0.01), simp(0.02)), '\n',
      'Реальная погрешность: ', simp(0.01) - (np.exp(1) - 1), '\n')

