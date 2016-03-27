def search(s):
    n = len(s)
    a = [[0 for i in range(n)] for i in range(n)]
    directions = [row[:] for row in a]
    for i in range(0, n):
        a[i][i] = 1
    for i in range(1, n):
        for j in range(0, n - i):
            if s[i + j] == s[j]:
                a[i + j][j] = a[i + j - 1][j + 1] + 2
                directions[i + j][j] = "diag"
            elif a[i - 1 + j][j] >= a[i + j][j + 1]:
                a[i + j][j] = a[i - 1 + j][j]
                directions[i + j][j] = "up"
            else:
                a[i + j][j] = a[i + j][j + 1]
                directions[i + j][j] = "right"
    result = ''
    i = n - 1
    j = 0
    while i > j:
        if directions[i][j] == "up":
            i -= 1
        elif directions[i][j] == "right":
            j += 1
        else:
            result += s[i]
            i -= 1
            j += 1
    if i == j:
        result = result + s[i] + result[::-1]
    else:
        result = result + result[::-1]
    return result


if __name__ == '__main__':
    s = input()
    print(search(s))
