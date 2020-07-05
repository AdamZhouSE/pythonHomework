def handshaking(n):
    global f
    if n==0 or n==2: return
    times=0
    for i in range(0,n,2):
        if f[i]==1: handshaking(i)
        if f[n-2-i]==1: handshaking(n-2-i)
        times+=f[i]*f[n-2-i]
    f[n]=times


t=int(input())
while t:
    n=int(input())
    f=[]
    for i in range(n+1):
        f.append(1)
    handshaking(n)
    print(f[n])
    t-=1