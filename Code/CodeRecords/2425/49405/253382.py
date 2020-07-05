T = int(input())
for t in range(T):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [(k - m) for m in a]
    b.sort(key=lambda x: abs(x))
    print(m + b[0])