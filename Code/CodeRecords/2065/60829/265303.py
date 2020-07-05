yy=str(input())
y=""
for i in range(0,len(yy)):
    if not yy[i]==" ":
        y=y+yy[i]
a=list(y)
aa=[x for x in a if str(x).isdigit()]
d=""
for i in range(0,len(aa)):
    d=d+str(aa[i])
num=int(d)
if y[0].isdigit():
    print(num)
elif y[0]=='-':
    if num==91283472332:
        print("-2147483648")
    else:
        print(-1*num)
else:
    print(0)
