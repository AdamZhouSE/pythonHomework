T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(' '.join(map(str, sorted(a + b))), end=' \n')