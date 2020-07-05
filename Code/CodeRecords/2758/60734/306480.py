def comb(x,y):
    ans = 1
    for i in range(x,0,-1):
        ans = ans*y/i
        y-=1
    return int(ans)


n, m = input().split(' ')
n = int(n)
m = int(m)

print((comb(n-1,n*m)//n)%10007)