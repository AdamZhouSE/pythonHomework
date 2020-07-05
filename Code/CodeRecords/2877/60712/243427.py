n = int(input())
list1 = list(map(int, input().split()))
min_1 = 0
min_2 = 0
temp = 0
i = 0
j = n
for k in range(n):
    temp = temp + list1[i]
    if temp < min_1:
        mix_1 = temp
        i = k
temp = 0
for k in range(n - 1, -1, -1):
    temp = temp + list1[k]
    if temp < min_2:
        min_2 = temp
        j = k
temp = 0
if min_1 < min_2:
    for k in range(k + 1, n, -1):
        temp += list1[k]
    print(temp - min_1)
else:
    for k in range(0, j):
        temp += list1[k]
    print(temp - min_2)
