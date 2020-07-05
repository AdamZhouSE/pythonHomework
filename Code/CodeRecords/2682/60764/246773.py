T=int(input())
for t in range(T):
    n,l,r=list(map(int,input().split()))
    bit=[]
    while n!=0:
        bit.append(n%2)
        n=int(n/2)
    for i in range(l-1,r):
        bit[i]=1
    res=0
    for j in range(len(bit)):
        if bit[j]==1:
            res+=int(pow(2,j))
    print(res)