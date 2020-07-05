def find(b,x,y,a,n):
    tmp=b[x]
    tbp=b[x]
    if y-x==1 and b[x]<b[y]:
        a=-1
        n=-1
    elif x==y:
        a=-2
        n=-2
    elif y-x==1 and b[x]>b[y]:
        a=-3
        n=-3
    for i in range(x+1,y+1):
        if tmp<b[i]:
            tmp=b[i]
            a=i
    for i in range(x+1,y+1):
        if tbp>b[i]:
            tbp=b[i]
            n=i
bb=str(input()).split(",")
b=[]
for i in bb:
    b.append(int(i))
count=0
x=0
y=len(b)-1
a=y
n=0
for i in range(0,len(b)):
    find(b,x,y,a,n)
    if a==n:
        if a==-1:
            count=count+2
        elif a==-2:
            count=count+1
        else:
            pass
        break
print(count)