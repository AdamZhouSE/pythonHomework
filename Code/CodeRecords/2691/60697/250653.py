def findPartition(arr, n):
    sums = 0
    i, j = 0, 0
    for i in range(n):
        sums += arr[i]

    part = [[True for i in range(n + 1)]
            for j in range(sums // 2 + 1)]

    for i in range(0, n + 1):
        part[0][i] = True

    for i in range(1, sums // 2 + 1):
        part[i][0] = False

    for i in range(1, sums // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    for i in range(sums // 2, 0, -1):
        for j in range(1, n + 1):
            if (part[i][j]) == 1:
                return sums - 2 * i

    return -1

t=int(input())
sizes=[]
nums=[]
for i in range(t):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
for i in range(t):
    res=findPartition(nums[i],sizes[i])
    print(res)