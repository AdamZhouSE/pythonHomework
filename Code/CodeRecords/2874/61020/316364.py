n = int(input())
a = list(map(int, input().split(" ")))
l = [3, 2, 1, 3]
rest = 0
last = 0
for i in range(n):
    if a[i] == 0:
        rest += 1
        last = 0
    elif a[i] == 3:
        last = l[last]
    else:
        if last == a[i]:
            rest += 1
            last = 0
        else:
            last = a[i]

print(rest)
