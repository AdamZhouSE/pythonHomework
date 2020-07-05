t=int(input())
for _ in range(t):
    ans=0
    x=int(input())
    for i in range(1,x+1):
        ans+=i**5
    print(ans)