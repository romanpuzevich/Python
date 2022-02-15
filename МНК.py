import numpy as np
import matplotlib.pyplot as plt

years = np.empty(26)
j = 20
for i in range(0, 26):
    years[i] = j
    j += 1

sm = [431, 409, 429, 422, 530, 505, 459, 499, 526,
      563, 587, 595, 647, 669, 746, 760, 778, 828,
      846, 836, 916, 956, 1014, 1076, 1134, 1024]\

def mnk(begin, end):
    b = begin - 20
    e = end - 19

    years = np.zeros(26)
    j = 20
    for i in range(0, 26):
        years[i] = j
        j += 1

    sm = [431, 409, 429, 422, 530, 505, 459, 499, 526,
          563, 587, 595, 647, 669, 746, 760, 778, 828,
          846, 836, 916, 956, 1014, 1076, 1134, 1024]

    A = np.zeros(shape=(e - b, 2))

    for i in range(0, e - b):
        for j in range(0, 2):
            if j == 0:
                A[i][j] = years[i + b]
            else:
                A[i][j] = 1

    A_tr = A.transpose()

    B = np.zeros(shape=(2, 2))

    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, e - b):
                B[i][j] += A_tr[i][k]*A[k][j]

    f = np.zeros(2)
    for i in range(0, 2):
        for j in range(0, e - b):
            f[i] += A_tr[i][j]*sm[j + b]

    x = np.linalg.solve(B, f)
    print(np.linalg.cond(B))
    x_ = np.arange(begin, end, 0.01)
    y_ = x[0]*x_ + x[1]
    return x_, y_

def f0(x):
    if (x >= 20 and x < 28):
        return (-x/8 + 7/2)
    else:
        return 0

def f1(x):
    if (x >= 20 and x <= 28):
        return (x/8 - 5/2)
    elif (x > 28 and x < 39):
        return (-x/11 + 39/11)
    else:
        return 0

def f2(x):
    if (x > 28 and x <= 39):
        return (x/11 - 28/11)
    elif (x > 39 and x <= 45):
        return (-x/6 + 15/2)
    else:
        return 0

def f3(x):
    if (x >= 39 and x <= 45):
        return (x/6 - 13/2)
    else:
        return 0

def mnk4():
    A = np.zeros(shape=(26, 4))
    for i in range(0, 26):
        A[i][0] = f0(years[i])
    for i in range(0, 26):
        A[i][1] = f1(years[i])
    for i in range(0, 26):
        A[i][2] = f2(years[i])
    for i in range(0, 26):
        A[i][3] = f3(years[i])

    A_tr = A.transpose()

    B = np.zeros(shape=(4, 4))

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 26):
                B[i][j] += A_tr[i][k]*A[k][j]

    f = np.zeros(4)

    for i in range(0, 4):
        for j in range(0, 26):
            f[i] += A_tr[i][j] * sm[j]

    print(np.linalg.cond(B))
    x = np.linalg.solve(B, f)
    return x

koeff = []
koeff[:] = mnk4()


x4 = np.arange(20, 28.1, 0.1)
y4 = koeff[0]*(-x4/8 + 7/2) + koeff[1]*(x4/8 - 5/2)

x5 = np.arange(28, 39.1, 0.1)
y5 = koeff[1]*(-x5/11 + 39/11) + koeff[2]*(x5/11 - 28/11)

x6 = np.arange(39, 45.1, 0.1)
y6 = koeff[2]*(-x6/6 + 15/2) + koeff[3]*(x6/6 - 13/2)

plt.plot(years, sm, 'o ', x4, y4, x5, y5, x6, y6)

x, y = mnk(20, 45)
x1, y1 = mnk(20, 28)
x2, y2 = mnk(28, 39)
x3, y3 = mnk(39, 45)
plt.plot(x, y, x1, y1, x2, y2, x3, y3)



'''

'''



plt.show()
