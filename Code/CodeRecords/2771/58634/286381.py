t = int(input())
for i in range(t):
    n = int(input())
    if pow(int(pow(n, 0.5)), 2) == n:
        print(1)
    else:
        print(0)