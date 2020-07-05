t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    num = 0
    pairs = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                if [min(arr[i], arr[j]), max(arr[i], arr[j])] not in pairs:
                    pairs.append([min(arr[i], arr[j]), max(arr[i], arr[j])])
                    num += 1
                else:
                    continue
    print(num)
