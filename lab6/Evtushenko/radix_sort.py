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


def sort(a):
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


def radix_sort(a):
    positive = []
    negative = []
    for i in a:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(i)
    positive = sort(positive)
    negative = [-x for x in negative]
    negative = sort(negative)
    negative = [-x for x in negative]
    negative.reverse()
    for i in positive:
        negative.append(i)
    return negative


if __name__ == '__main__':
    a = [int(i) for i in stdin.readline().split()]
    a = radix_sort(a)
    for i in a:
        stdout.write(str(i) + ' ')
