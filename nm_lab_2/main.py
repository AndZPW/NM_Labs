import numpy as np
from random import random

def error():
    f = open("output2.txt", 'w')
    f.write('The system has infinite number of answers...\n')
    f.close()
    raise Exception('The system has infinite number of answers...')

class Random:
    def __init__(self, coef: float = 14.88):
        self.__coef = coef

    def randomMatrix(self, sizeM: int) -> np.array:
        resM = [[0.0] * (sizeM + 1) for _ in range(sizeM)]
        for i in range(sizeM):
            for j in range(sizeM + 1):
                resM[i][j] = random() * self.__coef + i * j
        return np.array(resM)


class IO:
    @staticmethod
    def read(file_name: str) -> list:
        f = open(file_name)
        a = []
        for i in f:
            a.append(list(map(float, i.split())))
        f.close()
        return [np.array(a), len(a)]

    @staticmethod
    def write(file_name: str, answer: list, det: float) -> None:
        f = open(file_name, 'w')

        for i in answer:
            for j in i:
                f.write(f"{j}\n")
        f.write(f"Det: {det}\n")
        f.close()


class Matrix_Solver:

    @staticmethod
    def det(matrix: np.array) -> float:
        res: float = 1.0
        for i in range(len(matrix)):
            res *= matrix[i][i]
        return res


    @staticmethod
    def result(m: np.array, n: int) -> list:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if m[i,i]==0 and m[j,i]==0:
                    error()
                c = m[i, i] / (m[i, i] ** 2 + m[j, i] ** 2) ** 0.5
                s = m[j, i] / (m[i, i] ** 2 + m[j, i] ** 2) ** 0.5
                tmp1 = m[i, :] * c + m[j, :] * s
                tmp2 = m[i, :] * -s + m[j, :] * c
                m[i, :] = tmp1
                m[j, :] = tmp2
        print(m)
        if Matrix_Solver.__is_singular(m):
            error()
        else:
            x = np.matrix([0.0 for i in range(n)]).T
            for k in range(n - 1, -1, -1):
                x[k, 0] = (m[k, -1] - m[k, k:n] * x[k:n, 0]) / m[k, k]

            return x.tolist()

    @staticmethod
    def __is_singular(matrix: np.array) -> bool: return np.any(np.diag(matrix) == 0)


def test_max_matrix_size() -> None:
    size: int = int(input())
    my_random: Random = Random()
    random_matrix: np.array = my_random.randomMatrix(size)
    print(Matrix_Solver.result(random_matrix,size))


def main() -> None:
    matrix, n = IO.read("input3.txt")
    IO.write("output2.txt", Matrix_Solver.result(matrix, n), Matrix_Solver.det(matrix))


if __name__ == '__main__':
    main()
