s=input().split(" ")
n=int(s[0])
m=int(s[1])
num=input().split(" ")
for e in range(len(num)):
    num[e]=int(num[e])
result=[]
for i in range(m):
    sum=0
    dou=0
    a=input()
    a=a.split(" ")
    if a[len(a)-1]==" ":
        a=a[0:len(a)-1]
    for j in range(len(a)):
        a[j]=int(a[j])
    if a[0]==1:
        x=a[1]
        y=a[2]
        k=a[3]
        for l in range(x-1,y):
            num[l]=num[l]+k
    elif a[0]==2:
        x=a[1]
        y=a[2]
        for v in range(x-1,y):
            sum=sum+num[v]
        result.append(format(sum/(y-x+1),'.4f'))
    else:
        x=a[1]
        y=a[2]
        for v in range(x-1,y):
            sum=sum+num[v]
        for p in range(x-1,y):
            dou=dou+(num[p]-sum/(y-x+1))*(num[p]-sum/(y-x+1))
        result.append(format(dou/(y-x+1),'.4f'))
for f in range(len(result)):
    print(result[f])