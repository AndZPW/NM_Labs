from numpy import *

def swapRows(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        temp = v[i].copy()
        v[i] = v[j]
        v[j] = temp


def swapCols(v, i, j):
    temp = v[:, j].copy()
    v[:, j] = v[:, i]
    v[:, i] = temp


def gaussPivot(a, b, tol=1.0e-12):
    n = len(b)
    s = zeros((n), dtype=float64)
    for i in range(n):
        print(max(abs(a[i, :])))
        s[i] = max(abs(a[i, :]))
    for k in range(0, n - 1):
        # Перестановка рядків, якщо потрібна
        p = int(argmax(abs(a[k:n, k]) / s[k:n])) + k
        if abs(a[p, k]) < tol: print('Матриця  сингулярна')
        if p != k:
            swapRows(b, k, p)
            swapRows(s, k, p)
            swapRows(a, k, p)
            # Фаза  виключення
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]
        if abs(a[n - 1, n - 1]) < tol: print('Матриця  сингулярна')
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    return b
d=[[0, 1, -6, -4 ],[3, -1, -6, -4],[2, 3, 9, 2],[3,2,3,8]]
s=array(d)
print(s)
pp=array([6.0,2.0,6.0,-7.0])
print(max(s[0,:]))
print(gaussPivot(s,pp))