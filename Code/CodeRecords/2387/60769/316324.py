def solve(l, todo):
    ptr = []
    record = []
    for i in range(len(l)):
        if todo[1] <= l[i] <= todo[2]:
            ptr.append(i)
            record.append(l[i])
    if todo[0] == 0:
        record = sorted(record)
    else:
        record = sorted(record, reverse=True)
    for i in range(len(ptr)):
        l[ptr[i]] = record[i]
    # print(l)
    return l


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
for j in range(k):
    temp = list(map(int, input().split()))
    arr = solve(arr, temp)
index = int(input())
print(arr[index])
