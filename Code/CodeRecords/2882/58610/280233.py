length = eval(input())
arr = list(map(int, input().split(' ')))
pos1 = 0
try:
    while arr[pos1 + 1] > arr[pos1]:
        pos1 += 1
    pos2 = pos1
    while arr[pos2 + 1] == arr[pos2]:
        pos2 += 1
except IndexError:
    print('YES')
    exit()
pos3 = pos2
while pos3 < length - 1 and arr[pos3 + 1] < arr[pos3]:
    pos3 += 1
print('YES') if pos3 == length - 1 else print('NO')