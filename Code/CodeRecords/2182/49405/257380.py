T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    s = 0
    for i in range(2, n + 1):
        s = (s + k) % i
    print(s + 1)