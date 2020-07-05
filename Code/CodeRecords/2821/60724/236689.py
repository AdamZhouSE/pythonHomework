cardNo=int(input())
a=input().split()
last=len(a)-1
s=0
d=0
temp=0
for i in range(last+1):
    if i%2==0:
        if int(a[0])<int(a[last]):
            s=s+int(a[last])
            del a[last]
            last=last-1
        else:
            s=s+int(a[0])
            del a[0]
            last=last-1
    else:
        if int(a[0])<int(a[last]):
            d=d+int(a[last])
            del a[last]
            last=last-1
        else:
            d=d+int(a[0])
            del a[0]
            last=last-1
print(str(s)+" "+str(d))