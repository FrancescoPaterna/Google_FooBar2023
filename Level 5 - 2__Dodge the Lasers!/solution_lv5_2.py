from math import floor

#based on Concrete Matematics by Graham Knuth Patashnik
def gauss(n):
    return n * (n + 1) / 2


def graham(n):
    a = floor(n ** (1 / 2))
    return int(n * a - (1.0 / 3) * (a ** 3) - (1.0 / 2) * (a ** 2) - (1.0 / 6) * (a))


def solution(s):
    return str(gauss(int(s)) + graham(int(s)))

