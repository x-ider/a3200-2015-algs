import math


def sieve(n):
    a = [simple(x) for x in range(1, n + 1)]
    return a


def simple(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


n = input("Enter range: ")
print(sieve(int(n)))