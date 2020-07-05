n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    while arr[i] % 2 == 0:
        arr[i] //= 2
    while arr[i] % 3 == 0:
        arr[i] //= 3
print('Yes' if arr.count(arr[0]) == len(arr) else 'No')