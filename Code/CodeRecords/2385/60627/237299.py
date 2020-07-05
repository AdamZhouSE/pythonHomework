# 47
n = int(input())
def c(m,n):
    u_s = 1
    d_s = 1
    for i in range(1,n+1):
        u_s *= i
    for i in range(1,m+1):
        d_s *= i
    for i in range(1,n-m+1):
        d_s *= i
    return int(u_s/d_s)
for i in range(n):
    t = 0
    k = int(input())
    if k%2 == 0:
        for i in range(1,int(k/2)+1):
            t += c(i,k-i+1)
    else:
        for i in range(1,int(k/2)+2):
            t += c(i,k-i+1)
    print(t + 1)
