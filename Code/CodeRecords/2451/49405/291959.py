a = [-1] + list(map(int, input().split(","))) + [99999999]
t = int(input())
for i in range(len(a) - 1):
    if a[i] < t and a[i + 1] >= t:
        if a[i + 1] == t: print(i)
        else: print(i - 1)
        exit()