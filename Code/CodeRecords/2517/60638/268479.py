listA=list(map(int,input().split(",")))
listB=list(map(int,input().split(",")))
listC=list(map(int,input().split(",")))
listD=list(map(int,input().split(",")))
sum=0
for i in range(0,len(listA)):
    for j in range(0,len(listB)):
        for n in range(0,len(listC)):
            for m in range(0,len(listD)):
                if listA[i]+listB[j]+listC[n]+listD[m]==0:
                    sum=sum+1
print(sum)