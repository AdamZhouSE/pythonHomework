nc=input().split()
n=int(nc[0])
c=int(nc[1])
time=input().split()
for i in range(0,len(time)):
    time[i]=int(time[i])
cnt=1
for i in range(1,len(time)):
    if time[i]-time[i-1]<=c:
        cnt+=1
    else:
        cnt=1
print(cnt)