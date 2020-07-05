T=int(input())
for i in range(T):
    k=int(input().split()[2])
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for j in range(len(B)):
        A.append(B[j])
    A=sorted(A)
    print(A[k-1])