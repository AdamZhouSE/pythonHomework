T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        if i == N - 1:
            print(arr[i])
            break
        if arr[i] >= max(arr[i+1:]):
            print(arr[i], end=" ")
