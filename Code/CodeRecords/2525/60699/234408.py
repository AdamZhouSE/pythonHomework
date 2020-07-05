startTime=input()
startTime=startTime[1:len(startTime)-1]
startTime=list(map(int,startTime.split(',')))
endTime=input()
endTime=endTime[1:len(endTime)-1]
endTime=list(map(int,endTime.split(',')))
profit=input()
profit= profit[1:len( profit)-1]
profit=list(map(int, profit.split(',')))
n = len(startTime)
h = sorted(zip(endTime, startTime, endTime, profit))

w = [0] * n
for i in range(n - 1, -1, -1):
    flag = 0
    for j in range(i - 1, -1, -1):
        if h[j][2] <= h[i][1]:
            flag = 1
            w[i] = j
            break
    if flag == 0:
        w[i] = -1
OPT = [0] * (n + 1)
for i in range(n):
    OPT[i + 1] = max(OPT[i], h[i][3] + OPT[w[i] + 1])
print(OPT[n])
