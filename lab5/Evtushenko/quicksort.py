from sys import stdin, stdout
import random


def quick_sort(a, l, r):
    if l < r:
        t = partition(a, l, r)
        left_border, right_border = t
        quick_sort(a, l, left_border)
        quick_sort(a, right_border, r)


def partition(a, l, r):
    pivot_id = random.randint(l, r)
    a[l], a[pivot_id] = a[pivot_id], a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= a[l]:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    k = j
    for i in range(l, k - 1):
        if a[i] == a[j]:
            k -= 1
            a[i], a[k] = a[k], a[i]
    return k - 1, j + 1

if __name__ == '__main__':
    a = [int(i) for i in stdin.readline().split()]
    quick_sort(a, 0, len(a) - 1)
    for i in a:
        stdout.write(str(i) + ' ')
