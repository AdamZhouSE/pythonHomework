t=int(input())
for i in range(t):
    a,b,m=map(int,input().split(" "))
    k=0
    for j in range(a,b+1):
        if(j%m==0):
            k+=1
    print(k)