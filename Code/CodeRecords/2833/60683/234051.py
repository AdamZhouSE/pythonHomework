n = eval(input())
remains = [int(x) for x in input().split()]
remain = sum(remains)
contains = [int(x) for x in input().split()]
max1 = max2 = -1
for i in range(n):
    if contains[i] > max1:
        max2 = max1
        max1 = contains[i]
    elif contains[i] > max2:
        max2 = contains[i]
if remain <= max2 + max1:
    print('YES')
else:
    print('NO')