n, k = [int(x) for x in input().split()]
times = [0 for _ in range(n)]
ans = 0
prices = [int(x) for x in input().split()]
planes = []
for i in range(n):
    planes.append([prices[i], i])
planes.sort()
planes.reverse()
fly_time = []
for i in range(n):
    j = 0
    if planes[i][1] <= k:
        j = 0
    else:
        j = planes[i][1]-k
    while True:
        if times[j] == 0:
            ans += planes[i][0]*(j+k-planes[i][1])
            times[j] = 1
            fly_time.append([planes[i][1], j+k])
            break
        else:
            j += 1
print(ans)
fly_time.sort()
for res in fly_time:
    print(res[1]+1, end=' ')