T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(sum(arr[:K]))

