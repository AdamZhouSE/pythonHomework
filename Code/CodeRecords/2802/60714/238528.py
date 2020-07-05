from math import ceil

n, m = [int(x) for x in input().split()]
num = [ceil(int(x) / m) for x in input().split()]
print(num)
for i in range(n - 1, -1, -1):
    if num[i] == max(num):
        print(i + 1)
        break
