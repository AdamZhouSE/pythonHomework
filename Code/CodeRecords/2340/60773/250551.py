num=int(input())
for i in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    sum=0
    for k in range(n):
        l[k]=int(l[k])
    square=0
    for j in range(1,len(l)-1,1):
        n1=max(l[:j])
        n2=max(l[j+1:])
        n3=min(n1,n2)
        if l[j]<n3:
            square=square+n3-l[j]

    print(square)