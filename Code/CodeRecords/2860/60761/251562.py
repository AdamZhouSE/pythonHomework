n=int(input())
xs=[]
ys=[]
for i in range(n):
    x,y=map(int,input().split(" "))
    if x not in xs:
        xs.append(x)
    if y not in ys:
        ys.append(y)
print(min(len(xs),len(ys))-1)