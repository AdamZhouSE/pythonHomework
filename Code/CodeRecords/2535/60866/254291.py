def paixu(a):
    j=0
    n=0
    i=0
    while(n!=len(a)):
        while(a[i]!=n):
            i=i+1
        i=i+1
        n=i
        j=j+1     
    print(j)   
a=input()
a=list(a)
paixu(a)