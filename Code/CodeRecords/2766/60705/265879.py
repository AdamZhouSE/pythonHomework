test = int(input())
for i in range(0, test):
    n = int(input())
    if n % 5 == 0:
        print(-1)
    else:
        print(n % 5)
