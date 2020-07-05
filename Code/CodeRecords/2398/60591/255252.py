N,Tmax = list(map(int,input().strip().split(" ")))
milkTime = []
while(N != 0):
    milkTime.append(int(input()))
    N -= 1
for x in range(1,len(milkTime) + 1):
    tempT = 0
    res = milkTime[0:x]
    y = x
    time = 0
    while(y < len(milkTime)):
        minTime = min(res)
        for t in range(len(res)):
            res[t] -= minTime
        time += minTime
        for z in range(len(res)):
            if(res[z] == 0):
                res[z] = milkTime[y]
                y += 1
                if(y >= len(milkTime)):
                    break
    time += max(res)
    if(time <= Tmax):
        print(x)
        break