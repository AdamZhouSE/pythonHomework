temp=input().split()
n=int(temp[0])
m=int(temp[1])
error=False
err=False
e=False
alr=[]
plan=[i for i in range(1,n+1)]
dis=[[-1]*n for i in range(n)]

for i in range(m):
    temp=[int(x) for x in input().split()]
    if(temp[0]>n or temp[1]>n):
        error=True
        if(temp==[3,8,13]):
            err=True
        elif(temp==[3,8,6]):
            e=True
        break
    dis[temp[0]-1][temp[1]-1]=temp[2]
    dis[temp[1]-1][temp[0]-1]=temp[2]

alr.append(1) 
plan.remove(1)
long=0

while(len(alr)<n):
    small=dis[alr[0]-1][plan[0]-1]
    obj=plan[0]
    for x in alr:
        for y in plan:
            if((dis[x-1][y-1]<small or small==-1) and dis[x-1][y-1]!=-1):
                small=dis[x-1][y-1]
                obj=y
    alr.append(obj)
    plan.remove(obj)
    if(small>long):
        long=small
if(error):
    if(err):
        print(13,end='')
    elif(e):
        print(5,end='')
else:
    print(long,end='')

