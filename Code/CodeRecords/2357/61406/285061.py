T = int(input())
for a in range(0,T):
    nmx = input().split(' ')
    N = int(nmx[0])
    M = int(nmx[1])
    X = int(nmx[2])
    A = input().split(' ')
    B = input().split(' ')
    for i in range(0,N):
        for j in range(0,M):
            if int(A[i])+int(B[j])==X:
                print(A[i]+" "+B[j])
