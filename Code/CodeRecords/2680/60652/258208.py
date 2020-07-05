def path(M,N):
    if M==0 or N==0:
        return 0
    if M==1 and N==1:
        return 1
    return path(M-1,N)+path(M,N-1)


T=int(input())
for i in range(0,T):
    M,N=map(int,input().split())
    print(path(M,N))