from math import floor
def sum_of_floor_sqrt_2(start, end):
    result = 0
    for i in range(start, end + 1):
        result += math.floor(i * math.sqrt(2))
        print(math.floor(i * math.sqrt(2)))
    return int(result)


def gauss(n):
    return n*(n+1)/2


def graham(n):
    a = floor(n**(0.5))
    b = n*a
    c = (1.0/3) * (a**3)
    d = (1.0/2) * (a**2)
    e = (1.0/6) * (a)
    print(a,b,c,d,e)
    return int(b-c-d-e)


def solution(s):
    return graham(s)

