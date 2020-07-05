T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = 0
    for i in range(0, N - K + 2):
        if max_sum < sum(arr[i: i+K]):
            max_sum = sum(arr[i: i+K])
    print(max_sum)

