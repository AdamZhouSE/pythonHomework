t=int(input())
for ti in range(t):
    si=input().split(' ')
    n=int(si[0])
    m=int(si[1])
    x=int(si[2])
    A=input().split(' ')
    B=input().split(' ')
    for i in range(n):
        for j in range(m):
            if int(A[i])+int(B[j])==x:
                print(A[i],B[j])