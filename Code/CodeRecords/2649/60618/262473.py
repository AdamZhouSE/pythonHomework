t=int(input())
for i in range(0,t):
    n,l,r=map(eval,input().split())
    binn=list(bin(n)[2:])
    binn.reverse()
    for j in range(l-1,r-1):
        if binn[j]==0:
            n+=2**j
    print(n)