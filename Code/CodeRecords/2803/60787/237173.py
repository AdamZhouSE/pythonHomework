n,m=map(int,input().split())
lamp=[]
for i in range(0,m):
    lamp.append(False)
for i in range(0,n):
    magic=[int(j) for j in input().split()]
    for k in range(1,len(magic)):
        lamp[magic[k]-1]=True
if False in lamp:
    print("NO")
else:
    print("Yes")