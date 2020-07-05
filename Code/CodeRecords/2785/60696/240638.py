n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

possibilities = [[]]
for i in range(n):
    current_n = len(possibilities)
    for j in range(current_n):
        temp = [int(k) for k in possibilities[j]]
        temp.append(1)
        possibilities.append([t for t in temp])
        temp.pop(-1)
        temp.append(-1)
        possibilities.append([t for t in temp])
    possibilities = possibilities[current_n:]

is_able = False
for each in possibilities:
    temp = 0
    for i in range(n):
        temp += each[i] * nums[i]
    if temp == 0 or temp % 360 == 0:
        is_able = True
        break

if is_able:
    print('YES')
else:
    print('NO')
