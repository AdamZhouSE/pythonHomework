import functools,collections
# t=int(input())
# for i in range(t):
#     n=int(input())
#     p=[]
#     l = eval('[' + input().replace(' ', ',') + ']')
#     for j in l:
#         if j%3==0:
#             p.append(j)
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
l = eval('[' + input().replace(' ', ',') + ']')
t=l[0];x=l[1];y=l[2]
n=eval('[' + input().replace(' ', ',') + ']')
dx=abs(n[0]-x)
dy=abs(n[1]-y)
m=[(dx,dy)]
num=1
for i in range(t-1):
    n=eval('[' + input().replace(' ', ',') + ']')
    dx=abs(n[0]-x)
    dy=abs(n[1]-y)
    flag=0
    for j in m:
        if dx==0 and j[0]==0:
            flag=1
            break
        if dy==0 and j[1]==0:
            flag=1
            break
        if  dx!=0 and dy!=0 and j[0]/dx==j[1]/dy:
            flag=1
            break
    if flag==0:
        num+=1
        m.append((dx,dy))
print(num)
# m=collections.Counter(n)
