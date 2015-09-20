from sys import stdin

value = int(stdin.readline())
coins = [int(i) for i in stdin.readline().split()]
amount = len(coins)
coins.sort(reverse=True)

combination = [0] * amount
temp_value = value
i = 0
while temp_value >= coins[amount - 1]:
    if temp_value >= coins[i]:
        combination[i] = temp_value // coins[i]
        temp_value -= combination[i] * coins[i]
    i += 1
i = 0
while combination[i] == 0:
    i += 1
start = i
i = amount - 1
while combination[i] == 0:
    i -= 1
end = i
counter = 0
if temp_value == 0 and start != end:
    counter += 1

while start != amount - 1:
    drop_big_coin = False
    while not drop_big_coin:
        temp_value = value
        if start != end:
            combination[end] -= 1
        i = start
        while temp_value > coins[amount - 1]:
            if i <= end:
                temp_value -= combination[i] * coins[i]
                i += 1
            else:
                if temp_value >= coins[i]:
                    combination[i] = temp_value // coins[i]
                    temp_value -= combination[i] * coins[i]
                    if i == amount - 1:
                        for j in range(amount - 2, -1, -1):
                            if combination[j] != 0:
                                end = j
                                break
                    else:
                        end = i
                i += 1
        if temp_value == 0:
            counter += 1
        if start == end:
            drop_big_coin = True
    combination[start] -= 1
    if combination[start] == 0:
        start += 1
        combination[start] = value // coins[start]
    end = start
if value % coins[amount - 1] == 0:
    counter += 1
print(counter)