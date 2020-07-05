fir=input().split()
subNo=int(fir[0])
oritime=int(fir[1])
zlist=input().split()
zlist.sort()
totaltime=0
for i in range(subNo):
    if i==0:
        ac=oritime
    else:
        ac=ac-1
    if ac<1:
        ac=1
    totaltime=totaltime+ac*int(zlist[i])
print(totaltime)