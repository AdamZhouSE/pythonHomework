mapOL=[]
temp=input()[1:-1]

sum=0
judge=True
i=0
while(i<len(temp)):
    i=temp.index("[")
    j=temp.index("]")
    tmp=temp[i+1:j]
    tmp=list(map(int,tmp.split(",")))
    for k in tmp:
        sum+=k
    mapOL.append(tmp)
    temp=temp[j+1:]
    i=j
n=len(mapOL)

def length(mapOL,x,y,n,temp):
    maxDis=0
    i=0
    while i<n:
        j=0
        while(j<n):
            if(mapOL[i][j]==0):
                temp.append(abs(j-y)+abs(i-x))
            j+=1
        i+=1
    return maxDis

if(sum==0 or sum==n*n):
    print(-1)
else:
    res=[]
    i=0
    while i<n:
        j=0
        while j<n:
            if(mapOL[i][j]!=1):
                j+=1
                continue
            temp=[]
            length(mapOL,i,j,n,temp)
            res.append(temp)
            j+=1
        i+=1
    number=len(res[0])
    Dis=[999 for j in range(number)]
    j=0
    while(j<number):
        k=0
        while(k<len(res)):
            Dis[j]=min(Dis[j],res[k][j])
            k+=1
        j+=1
    print(max(Dis))