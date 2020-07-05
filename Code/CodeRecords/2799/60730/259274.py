m = int(input())
n = list(map(int, input().split()))
for i in range(m):
    while True:
        if n[i] % 2 == 0:
            n[i] = n[i] / 2
        else:
            break
for i in range(m):
    while True:
        if n[i] % 3 == 0:
            n[i] = n[i] / 3
        else:
            break
n = list(set(n))
if len(n) == 1:
    print("Yes")
else:
    print("No")
