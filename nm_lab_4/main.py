import numpy as np

A = [[-3.0, -3.0, 4.0], [0.0, -1.0, 0.0], [6.0, 2.0, -4.0]]
b = [[1.0, 2.0, 3.0]]


def get_base(A):
    base = list(np.zeros((len(A), len(A))))
    D = []
    for i in base:
        D.append(list(i))
    return D


def get_U(A):
    D = get_base(A)
    i = 0
    while i < len(A):
        k = i + 1
        while k < len(A):
            D[i][k] = -A[i][k]
            k = k + 1
        i = i + 1
    return np.mat(D)


def get_D(A):
    D = get_base(A)
    for i in A:
        D[A.index(i)][A.index(i)] = A[A.index(i)][A.index(i)]
    return np.mat(D)


def get_L(A, D, U):
    L = D - A - U
    return L


def get_B(D, L, U, w):
    B = (D - w * L).I * ((1 - w) * D + w * U)
    return B


def get_f(D, L, w, b):
    f = w * (D - w * L).I * (np.mat(b).T)
    return f


def matrix_to_list(x):
    d = []
    ans = []
    for i in x:
        d.append(i.tolist())
    for i in d:
        ans.append(i[0])
    return ans


def roll(B, f, x0):
    x = np.mat(x0).T
    y = B * x + f
    return matrix_to_list(y.T)


def main(A, b, x0, e, w):
    U = get_U(A)
    D = get_D(A)
    L = get_L(A, D, U)
    B = get_B(D, L, U, w)
    f = get_f(D, L, w, b)
    n = 0
    ans = []
    ans.append(x1)
    ans.append(x0)
    ans1 = []
    ans1.append(x1[0])
    ans1.append(x0[0])
    while abs(ans[-1][0][1] - ans[-2][0][1]) > e:
        n = n + 1
        x0 = roll(B, f, x0)
        ans.append(x0)
    for i in ans:
        ans1.append(i[0])
    return ans1, len(ans1) - 2


x1 = [[0.0,0.0,0.0]]
x0 = roll(A, b, x1)
e = 0.00001
w = 1
print(main(A, b, x0, e, w))
