from collections import Counter
from math import factorial

#greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def CF(c, n):
    cc= factorial(n)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b)
    return cc

def pwc(n):
    p = n*[0]
    p[0] = n  
    res = [] 
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partition = a[:k+2]
            res.append((partition, CF(partition,n)))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partition = a[:k+1]
        res.append((partition, CF(partition,n)))
    return res


def solution(w, h, s):
    n = max(w,h)
    sol=0
    for cpw in pwc(w):
        for cph in pwc(h):
            m=cpw[1]*cph[1]
            sol+=m*(s**sum([sum([gcd(i, j) for i in cpw[0]]) for j in cph[0]]))
    return str(sol//(factorial(w)*factorial(h)))

