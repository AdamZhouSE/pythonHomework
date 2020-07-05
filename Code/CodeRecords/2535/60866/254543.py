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
b=[]
for x in a:
    if x.isdigit():
        b.append(x)
b=[int(x) for x in b]
paixu(b)