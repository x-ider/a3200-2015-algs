from sys import stdin
import time
import random


def merge_sort(a, p, r, k):
    if r - p <= k:
        insertion_sort(a, p, r)
    else:
        q = (p + r) // 2
        merge_sort(a, p, q, k)
        merge_sort(a, q + 1, r, k)
        merge(a, p, q, r)


def merge(a, p, q, r):
    la = [a[x] for x in range(p, q + 1)]
    la.append(float('inf'))
    ra = [a[x] for x in range(q + 1, r + 1)]
    ra.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r + 1):
        if la[i] <= ra[j]:
            a[k] = la[i]
            i += 1
        else:
            a[k] = ra[j]
            j += 1


def insertion_sort(a, p, r):
    for i in range(p + 1, r + 1):
        j = i
        while j > p and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

if __name__ == '__main__':
    a = [int(i) for i in stdin.readline().split()]
    merge_sort(a, 0, len(a) - 1, 9)
    for i in a:
        print(i, end=' ')

"""
# k = 9 according to code below:

a = [random.randint(0, 1000) for j in range(10000)]
for i in range(20):
    b = a[:]
    begin_time = time.time()
    merge_sort(b, 0, len(b) - 1, i)
    print('k =', i, ';', 'time =', time.time() - begin_time)

# log:
# k = 0 ; time = 27.326635360717773
# k = 1 ; time = 26.7527756690979
# k = 2 ; time = 26.977256774902344
# k = 3 ; time = 28.030653715133667
# k = 4 ; time = 26.720345973968506
# k = 5 ; time = 27.163134574890137
# k = 6 ; time = 26.623233318328857
# k = 7 ; time = 26.739053964614868
# k = 8 ; time = 9.179063558578491
# k = 9 ; time = 8.280412912368774
# k = 10 ; time = 26.596410512924194
# k = 11 ; time = 26.588425397872925
# k = 12 ; time = 27.76680302619934
# k = 13 ; time = 27.787920475006104
# k = 14 ; time = 27.16067361831665
# k = 15 ; time = 26.69021439552307
# k = 16 ; time = 26.74723505973816
# k = 17 ; time = 26.88852047920227
# k = 18 ; time = 26.689921140670776
# k = 19 ; time = 27.40079689025879
"""
