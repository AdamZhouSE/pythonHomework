test = int(input())
for i in range(0, test):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    if n % 2 == 1:
        print(arr[n // 2])
    else:
        print((arr[int(n/2) - 1] + arr[int(n/2)]) // 2)
