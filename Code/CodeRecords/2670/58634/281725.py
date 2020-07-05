t = int(input())
for i in range(t):
    n = int(input())
    if n<=0:
        print(-n)
        continue
    temp = 2
    while temp<n:
        temp *= 2
    print(temp-1-n)
    