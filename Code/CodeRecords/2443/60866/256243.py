def paixu(a):
    length=len(a)
    b=[str(x) for x in a]
    a=b
    while length>1:
        for i in range(0,length-1):
            if(int(a[i]+a[i+1])<int(a[i+1]+a[i])):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
        length=length-1
    ans=''
    for i in a:
        ans=ans+i
    print(int(ans))
a=input()
a=eval(a)
paixu(a)