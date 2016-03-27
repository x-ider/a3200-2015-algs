def calculate_way(a):
    max = 0
    temp_max = 0
    current_high = 0
    current_min = float("inf")
    for x in a:
        if x >= current_high:
            if temp_max > max:
                max = temp_max
            current_high = x
            temp_max = 0
        else:
            temp_max += current_high - x
            if x < current_min:
                current_min = x
    return max

def calculate(a):
    there = calculate_way(a)
    a.reverse()
    from_there = calculate_way(a)
    return max(there, from_there)

if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    print(calculate(a))
