def n():
    a11, a12, a13 = map(float, input().split())
    a21, a22, a23 = map(float, input().split())
    a31, a32, a33 = map(float, input().split())
    d = 0
    n = 5
    k = 1
    for A in range(-n, n + 1):
        for B in range(-n, n + 1):
            for C in range(-n, n + 1):
                d1 = abs(A * a11 + B * a21 + C * a31)
                d2 = abs(A * a12 + B * a22 + C * a32)
                d3 = abs(A * a13 + B * a23 + C * a33)
                if k == 1:
                    d = d1 - d2 - d3
                if k == 2:
                    d = d2 - d1 - d3
                if k == 3:
                    d = d3 - d1 - d2

                if d > 0:
                    print(A, B, C)


import numpy as np

d = np.array([[1, 2], [3, 4]])

print(np.linalg.det(d))
print((np.triu(d)))


def is_singular(matrix) -> bool:
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
        return False


class Ultra_Magic:
    def __matrix_max_row(self, matrix, n) -> int:
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

    def result(self, matrix) -> int:
        p: int = 0
        for k in range(len(matrix) - 1):
            p += self.__matrix_max_row(matrix, k)
            for i in range(k + 1, len(matrix)):
                div = matrix[i][k] / matrix[k][k]
                matrix[i][-1] -= div * matrix[k][-1]
                for j in range(k, len(matrix)):
                    matrix[i][j] -= div * matrix[k][j]

        if is_singular(matrix):
            print('')
            return p
        return p



print(det(d, result(d)))
print(d)
