import numpy as np
import random as rd
import sys

def check_diagonal(m: np.array) -> bool:
    for i in range(len(m)):
        sum = 0
        for j in range(len(m)):
            sum = sum + abs(m[i][j])
        sum = sum - abs(m[i][i])

        if abs(m[i][i]) < sum:
            return False
    return True

def is_singular(matrix: np.array) -> bool:
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
        return False

class Ultra_Magic:
    __prs: int = 0

    @staticmethod
    def det(A1: np.array) -> float:
        res = 1.0
        for i in range(len(A1)):
            res *= A1[i][i]
        return res * (-1) ** Ultra_Magic.__prs

    @staticmethod
    def __matrix_max_row(matrix: np.array, n: int) -> int:
        max_el = matrix[n][n]
        max_r = n
        ct = 0
        for i in range(n + 1, len(matrix)):
            if abs(matrix[n][i]) > abs(max_el):
                max_el = matrix[n][i]
                max_r = i

            if max_r != n:
                ct += 1
                matrix[n], matrix[max_r] = matrix[max_r], matrix[n]

        return ct

    @staticmethod
    def result(matrix: np.array) -> int:
        p: int = 0
        print(len(matrix))
        for k in range(len(matrix) - 1):
            p += Ultra_Magic.__matrix_max_row(matrix, k)
            for i in range(k + 1, len(matrix)):
                div = matrix[i][k] / matrix[k][k]
                matrix[i][-1] -= div * matrix[k][-1]
                for j in range(k, len(matrix)):
                    matrix[i][j] -= div * matrix[k][j]
        if is_singular(matrix):
            singular_write("output_.txt")
            sys.exit(0)

        Ultra_Magic.__prs = p

        return p


def check(count: int, file_name: str) -> None:
    if count == -1:
        file = open(file_name, 'w')
        file.write("Метод не сходиться")
        file.close()


def singular_write(file_n: str) -> None:
    f = open(file_n, 'w')
    f.write("Матриця сингулярна\n")
    f.close()


def read(file_name: str) -> list:
    f = open(file_name)
    a = []
    b = []
    for i in f:
        p = [float(x) for x in i.split()]
        b.append(p[-1])

        p.pop(-1)
        a.append(p)

    f.close()
    return [a, b, len(b)]




def write(residual: float,file_name: str, x: list, count: int, w: float,  eps: float = 1.e-6) -> None:
    f = open(file_name, 'w')
    f.write(f"Точність: {eps}\n")
    f.write(f"Коефіцієнт релаксації: {w}\n")

    if 1 < w < 2:
        f.write("Це метод верхньої релаксації\n")
    elif 0 < w < 1:
        f.write("Це метод нижньої релаксації\n")
    elif w == 1:
        f.write("Це метод Зейделя\n")

    f.write(f"Кількість ітерацій: {count}\n")
    j = 1
    for i in x:
        f.write(f"x{j} = {i}\n")
        j += 1
    f.write(f"Похибка: {residual}")
    f.close()



def norm(a: np.array, b: np.array, x: np.array) -> float:
    return np.linalg.norm(np.dot(a, x) - b, ord=2)


def result(a: np.array, b: np.array, x: np.array, omega: float = 1.9, eps: float = 1.e-6) -> list:
    p = np.column_stack((a, b))
    if is_singular(p):
        singular_write("output_.txt")
        sys.exit(0)

    p = p.tolist()
    if not check_diagonal(p):
        Ultra_Magic.result(p)

    p = np.array(p)
    print(p)

    row = p.shape[0]
    a0 = p[:, 0: row]

    b0 = p[:, row]

    err = 100.
    j = 0
    while err > eps and j < 2500:
        i = 0
        while i < x.size:

            x[i] = (1 - omega) * x[i] - omega * (np.dot(a0[i, :], x) - b0[i] - a0[i, i] * x[i]) / a0[i, i]
            i = i + 1
        j = j + 1
        err = norm(a0, b0, x)

    return [x, j]


def change_matrix(a: np.array, b: np.array) -> np.array:
    p = np.column_stack((a, b))
    row = p.shape[0]
    print(row)
    o = [-1]*row
    for m in range(row):
        o[m] = max(abs(p[m, :])) - sum(abs(p[m, :]))
    print(p)
    return p


def zero_approximation(n: int) -> np.array: return np.zeros(n, dtype=float)


def random_approximation(n: int) -> np.array:
    res = np.zeros(n, dtype=float)
    for i in range(n):
        res[i] = rd.randrange(100, 500) / 100
    return res


def approximation(n: int, a: np.array) -> np.array:
    x = np.zeros(n, dtype=float)
    for i in range(n):
        x[i] = a[i][i]
    return x


def main():
    old_settings = np.seterr(all='ignore')
    a1, b1, n = read("C:/Users/makar/PycharmProjects/NM_Labs/nm_lab_3/input_2.txt")

    # w: float = float(input("Введіть коефіцієнт релаксації: "))
    # eps: float = float(input("Введіть точність: "))
    val: list = [float(x) for x in input().split()]
    file_out: str = "output_.txt"

    a: np.array = np.array(a1)
    b: np.array = np.array(b1)

    #x = zero_approximation(n)
    x = approximation(n, a)

    if is_singular(a):
        singular_write(file_out)
        return

    answers, count = result(np.copy(a), np.copy(b), (x), *val)
    check(count, file_out)

    residual = np.linalg.norm(np.dot(a, x) - b)
    print("Похибка:",residual)
    write(residual,file_out, answers, count, *val)




if __name__ == '__main__':
    main()

"""""
if m < row:
    big = np.argmax(abs(p[m:, m]))
else:
    big = 0
    b1 = big + m
    c = np.copy(p[b1, :])
    p[b1, :] = p[m, :]
    p[m, :] = c
"""""
