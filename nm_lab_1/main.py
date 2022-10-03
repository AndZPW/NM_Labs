from random import random
from sys import exit


def zeroVector(sizeV: int) -> list:
    return [0] * sizeV


def randomMatrix(sizeM: int) -> list[list]:
    resM = [[0.0] * (sizeM + 1) for _ in range(sizeM)]
    for i in range(sizeM):
        for j in range(sizeM + 1):
            resM[i][j] = random() * 14.88 + i * j

    return resM


class TxtUtil:
    @staticmethod
    def read(txt_path: str) -> list[list]:
        file = open(txt_path)
        resL = []
        for i in file:
            resL.append(list(map(float, i.split())))
        return resL

    @staticmethod
    def write(txt_path: str, answers: list, det: float) -> None:
        f = open(txt_path, 'w')
        for i in answers:
            f.write(str(i) + "\n")
        f.write(str(det))
        f.close()


class Gauss:
    @staticmethod
    def print_matrix(matrix: list[list]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=' ')
            print()

    @staticmethod
    def matrix_max_row(matrix: list[list], n: int) -> int:
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
    def result(matrix: list[list]) -> int:
        p: int = 0
        for k in range(len(matrix) - 1):
            p += Gauss.matrix_max_row(matrix, k)
            for i in range(k + 1, len(matrix)):
                div = matrix[i][k] / matrix[k][k]
                matrix[i][-1] -= div * matrix[k][-1]
                for j in range(k, len(matrix)):
                    matrix[i][j] -= div * matrix[k][j]
        Gauss.print_matrix(matrix)
        if Gauss.is_singular(matrix):
            print('')
            return p

        for i in range(len(matrix) - 1, -1, -1):
            try:
                result[i] = (
                                    matrix[i][-1]
                                    - sum(
                                [matrix[i][j] * result[j] for j in range(i + 1, len(matrix))]
                            )
                            ) \
                            / matrix[i][i]
            except ZeroDivisionError:
                f = open("output.txt", 'w')
                f.write("Система не має однозначного розв'язку")
                f.close()
                exit(0)
        return p

    @staticmethod
    def det(A1: list[list], p: int) -> float:
        res = 1.0
        for i in range(len(A1)):
            res *= A1[i][i]
        return res * (-1) ** p

    @staticmethod
    def is_singular(matrix: list[list]) -> bool:

        for i in range(len(matrix)):
            if not matrix[i][i]:
                return True
            return False

    @staticmethod
    def pick_nonzero_row(m, k):
        while k < m.shape[0] and not m[k, k]:
            k += 1
        return k


class Main:
    @staticmethod
    def main(A1: list[list], arr1: list) -> None:
        p: int = Gauss.result(A1)

        TxtUtil.write("output.txt", arr1, Gauss.det(A1, p))


if __name__ == '__main__':
    matrix: list[list] = TxtUtil.read("C:/Users/makar/PycharmProjects/NM_Labs/nm_lab_3/input_2.txt")

    result: list = zeroVector(len(matrix))
    Main.main(matrix, result)
