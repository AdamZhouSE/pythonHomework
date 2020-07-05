def crazyComputer(time,limit):
    if(limit==0):
        return 0
    cnt = 1
    for i in range(1,len(time)):
        if(time[i]-time[i-1]>limit):
            cnt = 1
        else:
            cnt += 1
    return cnt
temp = input().split(" ")
n = int(temp[0])
limit = int(temp[1])
temp = input().split(" ")
time = []
for t in temp:
    time.append(int(t))
print(crazyComputer(time,limit))

