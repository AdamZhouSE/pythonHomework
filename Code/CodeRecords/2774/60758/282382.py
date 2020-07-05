k=int(input())
for i in range(0,k):
    m,n=map(int,input().split())
    toy=list(map(int,input().split()))
    toy.sort()
    total=0
    for j in range(m):
        if(total<=n):
            total+=toy[j]
        elif:
            print(j-1)
            break
        elif(j=m-1):
            print(m)