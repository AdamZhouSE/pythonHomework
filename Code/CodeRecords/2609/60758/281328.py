n=int(input())
for i in range(0,n):
    l,k=map(int,input().split())
    num=list(map(int,input().split()))
    for i in num:
        if num.count(i)==1:
            k-=1
            if(k==0):
                print(i)
                break
    if(k!=0):
        print(-1)