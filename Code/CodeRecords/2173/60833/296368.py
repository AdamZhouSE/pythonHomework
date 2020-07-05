n=int(input())

for i in range(0,n):
    res=0
    k=int(input())
    for j in range(1,k+1):
        res+=int(j*j)
    print(res)