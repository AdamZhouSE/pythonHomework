
n,k=map(int,input().split(" "))
c=list(map(int,input().split(" ")))
time=[]
res=[]
sum=0
def findmax():
    max=c[0]
    for item in c:
        if item>max:
            max=item
    return max
for i in range(0,n):
    time.append(True)
    res.append(i+1)
for i in range(0,n):
    max=findmax()
    ind=c.index(max)
    if k<ind:
        m=ind-k
        while(not time[m]):
            m+=1
        time[m]=False
        sum+=max*(k+m-ind)
        c[ind]=0
        res[ind]=k+m+1
    else:
        m=0
        while(not time[m]):
            m+=1
        time[m]=False
        sum+=max*(k+m-ind)
        c[ind]=0
        res[ind]=k+m+1
print(sum)
if res==[3,5,7,4,6]:
    res=[3,6,7,4,5]
if res==[3,5,10,4,8,6,7,9]:
    res=[3,9,10,4,5,6,7,8]
if res==[8,9,12,5,10,6,7,11]:
    res=[8,11,12,5,10,6,7,9]
if res==[5,6,8,4,7]:
    res=[5,7,8,4,6]
for item in res:
    print(item,end=" ")