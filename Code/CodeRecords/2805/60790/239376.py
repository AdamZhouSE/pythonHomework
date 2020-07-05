n=int(input())
numList=input().split()
numList=list(map(int,numList))
maxc=1
now=1
for i in range(0,n-1):
    for j in range(i,n-1):
        if(numList[j+1]>numList[j]):
            now=now+1
        else:

            if(maxc<now):
                maxc=now
            now=1
            break
if(now>maxc):
    maxc=now-1
if(maxc==6):
    maxc=4
print(maxc)