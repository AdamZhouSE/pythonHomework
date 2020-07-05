t=int(input())
for i in range(t):
    n=int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    num=0
    for j in range(n):
        for k in range(n):
            if A[j]==B[j]+C[k]:
                num+=1
    print(num)

