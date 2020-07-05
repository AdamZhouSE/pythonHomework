num = int(input())
for j in range(num):
    n = int(input())
    A = list(map(int,input().split(" ")))
    B = list(map(int,input().split(" ")))
    C = list(map(int,input().split(" ")))
    count = 0
    for i in range(n):
        if A[i] - B[i] in C:
            count+=1
    print(count)