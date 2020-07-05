a=int(input())
for i in range(a):
    b=[int(x) for x in input().split()]
    m,n=b[0]-1,b[1]-1
    total=m+n
    i,j=0,0
    up=down=1
    while i<m:
        up*=(total-i)
        i+=1
    while j<m:
        down*=(m-j)
        j+=1
    print(int(up/down))