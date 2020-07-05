a=eval(input())
b=[]
for i in range(a):
    b.append([int(x) for x in input().split(",")])
xOy=xOz=yOz=0
k=[0 for i in range(a)]
for i in range(a):
    maxmum=0
    for j in range(a):
        if(b[i][j]>0):
            xOy+=1
        maxmum=max(maxmum,b[i][j])
        k[j]=max(k[j],b[i][j])

    xOz+=maxmum
for i in k:
    yOz+=i
print(xOy+xOz+yOz)

