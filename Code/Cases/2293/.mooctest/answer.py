nTests = int(input())

for _ in range(nTests):
    _ = input()
    arr  = list(map(int, input().split()))
    k = int(input())
    arr.sort()
    print(arr[k-1])