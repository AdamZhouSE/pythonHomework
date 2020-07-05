a,b=map(int,input().split());c=[]
for _ in range(b):
    f=int(input())%a;c+=[f]
    if c.count(f)>1:print(_+1);exit()
print(-1)