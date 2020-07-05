firline=input()
strlist=firline.split()
totalplace=int(strlist[0])
totalnum=int(strlist[1])
i=-1
a = []
for k in range(totalnum):
    temp=input()
    a.append(temp)
ifocc=[0]*totalplace
for k in range(totalnum):
    pNo=int(a[k])%totalplace
    if ifocc[pNo]==0:
        ifocc[pNo]=1
    else:
        i=k+1
        break
print(i)

