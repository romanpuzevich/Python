# переписать критерий остановки для метода итераций, допилить мнк, подумать над погрешностью,
# интерполяция, интеграл/производная.
import numpy as np
import matplotlib.pyplot as plt

years = [1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000]
population = [92228496, 106021537, 123202624, 132164569, 151325789,
              179323175, 203211926, 226545805, 248709873, 281421906]


# интерполяция методом Ньютона
def separated_differences(n):
    sum = 0
    for j in range(0, n+1):
        term = population[j]
        for l in range(0, n+1):
            if l != j:
                term /= (years[j] - years[l])
            else:
                term *= 1
        sum += term
    return sum


year = int(input('Введите год: '))
years.append(year)


def newtons_polinom(year):
    population = 0
    for i in range(0, 10):
        pop = separated_differences(i)
        for j in range(0, i):
            pop *= (year - years[j])
        population += pop
    return population
population.append(newtons_polinom(year))

print('Население интерполяцией Ньютона: ', newtons_polinom(year))
# результат вычисления населения методом Ньютона равен 827908399
# реальное население равно 308745538

# кубическая сплайн интерполяция c постоянным шагом
# S(x, k) = a_k + b_k(x-x_k) + c_k(x-x_k)^2 + d_k(x-x_k)^3 , x = [xk, xk+1]

h = 10
c = np.empty(10)
c[0] = 1
c[1] = 1
c[8] = 1
c[9] = 0

for i in range(2, 8):
    c[i] = (3*((population[i] - population[i-1]) / h - (population[i-1] - population[i-2]) / h) - h*c[i-2] - 4*h*c[i-1]) / h

b = np.empty(9)
for i in range(0, 9):
    b[i] = (population[i+1] - population[i]) / h - h*(c[i+1] + 2*c[i]) / 3

d = np.empty(9)
for i in range(0, 9):
    d[i] = (c[i+1] - c[i]) / (3*h)

a = np.empty(11)
a[:] = population[:]

for i in range(0, 9):
    x = np.arange(years[i], years[i+1] + 0.1, 0.1)
    y = a[i] + b[i]*(x - years[i]) + c[i]*(x - years[i])**2 + d[i]*(x - years[i])**3
    plt.plot(x, y)


x = np.arange(1910, 2020, 0.1)
y = newtons_polinom(x)
plt.plot(years, population, 'o', x, y)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Population')
plt.axis([1900, 2020, 0, 10**9])
plt.show()


