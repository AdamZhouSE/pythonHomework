def paixu(a):
    for i in range(0,len(a)):
        while(a[i]>=1 and a[i]<=len(a) and a[i]!=i+1):
            temp=a[a[i]-1]
            a[a[i]-1]=a[i]
            a[i]=temp
    for i in range(0,len(a)):
        if(a[i]!=i+1):
            print(i+1)
            return
    print(i+1)
a=input()
a=eval(a)
paixu(a)