y=str(input())
a=list(y)
aa=[x for x in a if str(x).isdigit()]
d=""
for i in range(0,len(aa)):
    d=d+str(i)
num=int(d)
if y[0].isdigit():
    print(num)
elif y[0]=='-':
    print(-1*num)
else:
    print(0)

