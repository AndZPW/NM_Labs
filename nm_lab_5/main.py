from math import pi, sin


def findX(a: float, b: float, eps: float = 0.0001) -> float:
    f = lambda x: x ** 2 - sin(pi * x)
    while abs(b - a) > eps:
        a = b - (b - a) * f(b) / (f(b) - f(a))
        b = a - (a - b) * f(a) / (f(a) - f(b))
    return b


def main() -> None:
    print(findX(*[float(x) for x in input().split()]))


if __name__ == '__main__':
    main()
