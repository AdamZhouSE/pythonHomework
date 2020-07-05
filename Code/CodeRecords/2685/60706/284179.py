t=int(input())
for i in range(t):
    n=int(input())
    ans=''
    if(n<9):
        ans=str(n)
        for j in range(n):
            ans=ans+'0'
    else:
        for j in range(n):
            ans=ans+'0'
        while(n>9):
            ans='9'+ans
            n=n-9
        ans=str(n)+ans
    print(ans)