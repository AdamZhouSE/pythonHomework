NK = input().split(" ")
n = int(NK[0])
k = int(NK[1])
costs = input().split(" ")
costs = list(map(int,costs))
departTimes = []
for i in range(n):
    departTimes.append(0)
for i in range(k+1,k+n+1):
    nowDepart = -1
    nowFee = -1
    for j in range(i):
        if j == n:
            break
        if costs[j] >= nowFee and departTimes[j] == 0:
            nowFee = costs[j]
            nowDepart = j
    departTimes[nowDepart] = i
cost = 0
for i in range(len(costs)):
    cost = cost + (departTimes[i]-i-1)*costs[i]
print(cost)
for i in departTimes:
    print(i,end=" ")