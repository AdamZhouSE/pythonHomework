All = int(input())

for q in range(0, All):
    n=int(input())
    ans=0
    i=0

    while pow(2,i)<=n:
        i+=1
    i-=1

    n-=pow(2,i)
    ans+=1

    while n>0:
        while pow(2,i)>n:
            i-=1
        n-=pow(2,i)
        ans+=1
    print(ans)

