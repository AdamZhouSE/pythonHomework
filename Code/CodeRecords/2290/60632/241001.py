t = int(input())
result = []
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    tmp = []
    for j in range(1, n):
        if arr[j] < arr[j-1]:
            tmp.append(arr[j])
        else:
            tmp.append(-1)
    tmp.append(-1)
    tmp.append('')
    result.append(tmp)
for i in result:
    print(*i)
