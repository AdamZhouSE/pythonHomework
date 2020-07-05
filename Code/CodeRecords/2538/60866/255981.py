def paixu(a):
    j=a[0]
    for i in range(0,len(a)):
        if(j<a[i]):
            j=a[i]
    print(j+1)
a=input()
a=eval(a)
paixu(a)