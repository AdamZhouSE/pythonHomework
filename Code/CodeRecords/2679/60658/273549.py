t = int(input())
for i in range(t):
    n = int(input())   
    ans = 0
    if n == 1:
        ans = 3
    elif n==2:
        ans=8
    elif n>=3:
        ans=1+2*n+(n**3-n)//2
    print(ans)