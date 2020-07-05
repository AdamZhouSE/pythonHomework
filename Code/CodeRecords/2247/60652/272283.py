a=list(map(int,input().split(',')))
n=len(a)
n1,n2=0,0
while n>0:
    for i in range(2):
        index=0
        if a[0]<a[n-1]:
            index=n-1
        if n%2==0:
            n1+=a[index]
        else:
            n2+=a[index]
        a.pop(index)
        n-=1
if n1>n2:
    print(True)
else:
    print(False)