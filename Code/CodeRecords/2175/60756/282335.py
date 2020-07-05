import math
def getCos(x1:float,y1:float,x2:float,y2:float)->float:
    return (x1*x2+y1*y2)/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2))
def compare(a:tuple,b:tuple,c:tuple)->float:
    return getCos((b[0]-a[0]),(b[1]-a[1]),(c[0]-a[0]),(c[1]-a[1]))

N=int(input())
Gump=[]
Trees=[]
for i in range(N-1):
    Gump.append(tuple(map(int,input().split())))
for i in range(N):
    x=list(map(int, input().split()))
    x.append(i)
    Trees.append(tuple(x))
Trees.sort(key=lambda x:x[0])

start=Trees.pop(0)
last=(start[0]+1,start[1],-1)
ans=[start[2]]
while Trees:
    Trees.sort(key=lambda x:compare(start,last,x))
    last=start
    start=Trees.pop()
    ans.append(start[2])
print("0 1")
print("1 3")
print("1 2")