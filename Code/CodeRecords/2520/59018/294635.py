def juzhen(R,C,r0,c0):
    print(r0,c0)
    for i in range(max(R,C)+1):
        for j in range(i):
            if (0<=r0-j and r0-j<R) and(0<=c0+i-j and c0+i-j<C):
                print(r0-j,c0+i-j)
            if (0 <= r0 - i+j and r0 - i+j < R) and (0 <= c0  - j and c0  - j < C):
                print(r0-i+j,c0-j)
            if (0 <= r0 + j and r0 + j < R) and (0 <= c0 - i + j and c0 - i + j < C):
                print(r0+j,c0 - i + j)
            if (0 <= r0 + i-j and r0 +i- j < R) and (0 <= c0 + j and c0 + j < C):
                print(r0+i-j,c0 + j)

R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
juzhen(R,C,r0,c0)
