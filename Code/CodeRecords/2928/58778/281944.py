n=int(input())
numlist=list(map(int,input().split( )))
x=min(numlist)
for i in range(len(numlist)-1,-1,-1):
    if (numlist[i]==x):
        break
t=i
thenumofnumbers=int(n/x)
theleft=n%x
countlist=[0]*9
countlist[t]=thenumofnumbers
thediflist=[z-x for z in numlist]
for i in range(len(numlist)-1,-1,-1):
    if(thediflist[i]>theleft):
        continue
    else:
        if(i!=t):
            countlist[i]=int(theleft/thediflist[i])
            theleft=theleft%thediflist[i]
            countlist[t]-=countlist[i]
for i in range(len(numlist)-1,-1,-1):
    if(countlist[i]!=0):
        for j in range(countlist[i]):
            print(i+1,end='')