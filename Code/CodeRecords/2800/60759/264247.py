n, diff = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
count = 0
pre = lst[0]
for i in range(1, n):
    while lst[i] <= pre:
        lst[i] += diff
        count += 1
    pre = lst[i]
print(count)
