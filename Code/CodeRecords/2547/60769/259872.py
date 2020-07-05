num = int(input())
for j in range(num):
    n = int(input())
    record = []
    arr = list(map(int, input().split()))
    d = int(input())
    if d == 0:
        for i in range(n-1):
            if arr[i] in arr[i+1:]:
                if arr[i] not in record:
                    record.append(arr[i])
    else:
        for i in range(n):
            if arr[i] - d in arr:
                if [arr[i], arr[i] - d] not in record:
                    record.append([arr[i], arr[i] - d])
    print(len(record))
