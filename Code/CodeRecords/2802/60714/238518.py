n, m = [int(x) for x in input().split()]
num = [int(x) // m for x in input().split()]
for i in range(n - 1, -1, -1):
    if num[i] is max(num):
        print(i + 1)
        break
