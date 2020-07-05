n=int(input())
for i in range(0,n):
    m=int(input())
    s=0
    for j in range(2,m+1):
        s=(s+2)%j
    print(s+1)