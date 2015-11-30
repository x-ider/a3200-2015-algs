def calculate(m, n):
    if len(m) == 0 or len(n) == 0:
        return max(len(n), len(m))
    if len(n) < len(m):
        m, n = n, m
    current_row = [i + 1 for i in range(len(m))]
    if m.find(n[0]) >= 0:
        for i in range(m.find(n[0]), len(m)):
            current_row[i] -= 1
    for i in range(1, len(n)):
        previous_row = current_row[:]
        for j in range(0, len(m)):
            add_to_m = add_to_mn = transposition = float("inf")
            if j > 0:
                add_to_m = current_row[j - 1] + 1
            add_to_n = previous_row[j] + 1
            if j > 0 and i > 0:
                if m[j] == n[i]:
                    add_to_mn = previous_row[j - 1]
                else:
                    add_to_mn = previous_row[j - 1] + 1
                if m[j] == n[i - 1] and m[j - 1] == n[i]:
                    transposition = previous_row[j - 1]
                else:
                    transposition = previous_row[j - 1] + 1
            current_row[j] = min(add_to_m, add_to_n, add_to_mn, transposition)
    return current_row[len(m) - 1]


if __name__ == '__main__':
    m = input()
    n = input()
    print(calculate(m, n))