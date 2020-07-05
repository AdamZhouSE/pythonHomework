T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = len(set(A) & set(B))
    print(ans)
