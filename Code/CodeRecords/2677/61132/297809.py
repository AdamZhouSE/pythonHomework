n = int(input())
for j in range(n):
    n=int(input())
    l=list(map(int,input().split()))
    Sum=0
    for i in range(n):
        for j in range(i+1,n):
            if l[i]^l[j]==0:
                Sum+=1
    print(Sum)