t = int(input())
result = []
for i in range(t):
    tmp = input()
    maxi = 0
    arr = [1 for j in range(len(tmp))]
    for j in range(1, len(tmp)):
        for k in range(j, -1, -1):
            if tmp[k] < tmp[j]:
                arr[j] = max(arr[j], arr[k]+1)
                maxi = max(maxi, arr[j])
    result.append(maxi)
for i in result:
    print(i)
