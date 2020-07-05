n = int(input())
for i in range(n):
    k = int(input())
    if k % 5 == 0:
        print(-1)
    else:
        print(k % 5)