n=int(input())
xs=[]
ys=[]
for i in range(n**2):
    x,y=map(int,input().split(" "))
    if x not in xs and y not in ys:
        xs.append(x)
        ys.append(y)
        if (len(xs)==n):
            print(i+1)
        else:
            print(i+1,end=" ")
        