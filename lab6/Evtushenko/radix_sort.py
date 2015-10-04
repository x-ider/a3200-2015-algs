from sys import stdin, stdout


def digits_founder(x):
    i = 0
    while x > 0:
        x //= 10
        i += 1
    return i


def n_digit(x, n):
    for i in range(1, n):
        x //= 10
    x %= 10
    return x


def radix_sort(a):
    if len(a) != 0:
        max = a[0]
        for i in a:
            if i > max:
                max = i
        for i in range(1, digits_founder(max) + 1):
            a = counting_sort(a, i)
    return a


def counting_sort(a, n):
    b = [n_digit(i, n) for i in a]
    d = a[:]
    c = [0] * 10
    for i in range(0, len(a)):
        c[b[i]] += 1
    for i in range(0, 10):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        d[c[b[i]] - 1] = a[i]
        c[b[i]] -= 1
    return d

if __name__ == '__main__':
    a = [int(i) for i in stdin.readline().split()]
    a = radix_sort(a)
    for i in a:
        stdout.write(str(i) + ' ')