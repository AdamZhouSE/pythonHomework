n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(n):
    index_min = arr.index(min(arr[i:])) + 1
    # print(index_min)
    res.append(index_min)
    if i == 0:
        arr = arr[:i] + arr[index_min - 1::-1]+arr[index_min:]
    else:
        arr = arr[:i] + arr[index_min - 1:i - 1:-1]+arr[index_min:]
    # print(arr)
for i in res:
    print(i,end=" ")
    