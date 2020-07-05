T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    print(' '.join(map(str, a[:k])), end=' \n')