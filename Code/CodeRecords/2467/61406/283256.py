T = int(input())
for a in range(0,T):
    row1 = input().split(' ')
    m = int(row1[0])
    n = int(row1[1])
    k = int(row1[2])
    A = input().split(' ')
    B = input().split(' ')
    for i in range(0,m):
        A[i] = int(A[i])
    for j in range(0,n):
        A.append(int(B[j]))
    A.sort()
    print(A[k-1])


