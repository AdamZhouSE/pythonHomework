t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    while n>1:
        if n%2==0:
            ans+=1
        else:
            ans+=2
        n//=2
    if n==1:
        ans+=1
    print(ans)