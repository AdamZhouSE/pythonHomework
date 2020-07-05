t = int(input())
for ti in range(t):
    n = int(input())
    A = input().split(' ')
    B = input().split(' ')
    C = input().split(' ')
    co=0
    for i in range(n):
            for k in range(n):
                if int(A[i])==int(B[i])+int(C[k]):
                    co=co+1
    print(co)