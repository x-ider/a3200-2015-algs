from sys import stdin, stdout
import time


def quick_sort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quick_sort(a, l, q - 1)
        quick_sort(a, q + 1, r)


def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


a = [int(i) for i in stdin.readline().split()]
begin_time = time.time()
quick_sort(a, 0, len(a) - 1)
stdout.write(str(time.time() - begin_time) +'\n')
for i in a:
    stdout.write(str(i) + ' ')