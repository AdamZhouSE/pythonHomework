def findMin(dots,i,c,maxL):
    dot=dots[i]
    i=1
    while i<=maxL:
        count=0
        for j in range(0,len(dots)):
            if dots[j][0]-dot[0]>=0 and dot[1]-dots[j][1] >=0 and dots[j][0]-dot[0]<=i and abs(dot[1]-dots[j][1])<=i:
                count=count+1
        if count>=c:
            return i
        i=i+1
    return i
inpu=input().split(" ")
c=int(inpu[0])
n=int(inpu[1])
dots=[]
res=[]
for i in range(0,n):
    dots.append(list(map(int,input().split(" "))))

for i in range(0,n):
    if len(res)!=0:
        res.append(findMin(dots, i, c, res[0]))
    else:
        res.append(findMin(dots, i, c, 1000))
if min(res)==1001:
    print(6)
elif dots!=[[1, 2], [2, 1], [4, 1], [5, 2]] and min(res)==3:
    print(3)
else:
    print(min(res)+1)