num = int(input())
for i in range(num):
    n = int(input())
    count = 0
    arr = sorted(list(map(int, input().split(" "))))
    for j in range(n // 2 + 1):
        sum = arr[-1 - j]
        for k in range(n - 1 - j):
            if sum - arr[k] in arr[k+1:]:
                count += 1
    if count == 0:
        print(-1)
    else:
        print(count)

