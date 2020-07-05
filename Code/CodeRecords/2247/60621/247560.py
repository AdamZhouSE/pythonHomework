a=[int(x) for x in input().split(",")]
alex=0
lee=0;flag=1
while len(a)>0:
    if flag==1:
        if(a[len(a)-1]>a[0]):
            alex+=a[len(a)-1]
            a.pop(len(a)-1)
        else:
            alex+=a[0]
            a.pop(0)
    else:
        if (a[len(a) - 1] > a[0]):
            lee+= a[len(a) - 1]
            a.pop(len(a) - 1)
        else:
            lee += a[0]
            a.pop(0)
    flag*=-1
print(alex>lee)