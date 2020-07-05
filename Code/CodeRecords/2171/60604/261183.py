n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    ji=[]
    ou=[]
    for i in range(l):
        if a[i]%2==0:
            ou.append(a[i])
        else:
            ji.append(a[i])
    for i in ji:
        ou.append(i)
    for i in ou:
        print(i,end=' ')
    print()