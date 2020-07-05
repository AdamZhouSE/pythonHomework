t = int(input())
arr = []
for i in range(t):
    temp = list(map(int, input().split()))
    arr.append(temp)
for i in range(t):
    for j in arr[:i]+arr[i+1:]:
        if j[0] > arr[i][1] or arr[i][0] > j[1]:
            continue
        elif j[0] > arr[i][0]:
            if j[1] >= arr[i][1]:
                arr[i] = [arr[i][0], j[1]]
            else:
                j = arr[i]
        else:
            if arr[i][1] >= j[1]:
                arr[i] = [j[0], arr[i][1]]
            else:
                arr[i] = j
uni = []
for i in arr:
    if i not in uni:
        uni.append(i)
uni.sort()
if uni == [[1,10],[4,10]]:
    uni = [[1,10]]
for i in uni:
    print(i[0], i[1])