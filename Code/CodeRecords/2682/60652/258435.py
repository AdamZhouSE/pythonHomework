T=int(input())
for n in range(0,T):
    N,L,R=map(int,input().split())
    a=list(bin(int(N))[2:])
    a.reverse()
    for i in range(L-1,R):
        if i>len(a):
            a.append('1')
        else:
            a[i]='1'
    a.reverse()
    print(int("".join(str(k) for k in a),2))