n,m=input().split(' ')
n,m=int(n),int(m)
ss=input()
a=[int(i) for i in ss.split(' ')]
for i in range(m):
    l,r=input().split(' ')
    l,r=int(l),int(r)
    n1,n2=0,0
    for j in a:
        if j==1:
            n1+=1
        else:
            n2+=1
    if (r-l)%2==1 and r-l<min(n1,n2)*2:
        print(1)
    else:
        print(0)