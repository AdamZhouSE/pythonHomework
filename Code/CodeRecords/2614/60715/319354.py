t=int(input())
for ttt in range(t):
    n=int(input())
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    C=[int(i) for i in input().split()]
    count=0
    for i in range(n):
        for k in range(n):
            if A[i]==B[i]+C[k]:
                count+=1
    print(count)