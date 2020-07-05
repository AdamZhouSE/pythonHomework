def shuzu(a,k,x):
    l=0
    r=len(a)-1
    length=len(a)
    b=[]
    while length>k:
        if abs(a[l]-x)>abs(a[r]-x):
            l=l+1
        else:
            r=r-1
        length=length-1
    for x in range(l,r+1):
        b.append(a[x])
    print(b)
a=input()
a=eval(a)
k=int(input())
x=int(input())
shuzu(a,k,x)