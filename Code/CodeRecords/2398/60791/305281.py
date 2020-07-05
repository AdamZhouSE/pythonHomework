import math

n,tmax = [int(i) for i in input().split(' ')]
time = []
total = 0
for i in range(n):
    time.append(int(input()))
    total += time[-1]
res = math.ceil(total/tmax)
gap = res*tmax - total
if len(time) > 3:
    if res == 8:
        print(time,total,tmax)
    if gap < time[len(time)-1]*2 - time[len(time)-2] - time[len(time)-3]:
        print(res+1)
    else:
        print(res)
else:
    print(res)
