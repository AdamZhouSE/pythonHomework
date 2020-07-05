t = int(input())
z=0
while z<t :
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    count=0
    for i in l :
        if k>=i :
            k=k-i
            count=count+1
    print(count)
    z=z+1