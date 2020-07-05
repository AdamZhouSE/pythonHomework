questNum = int(input())

for quest in range(questNum):
    n = int(input())
    A = input().split(' ')
    B = input().split(' ')
    C = input().split(' ')
    
    for i in range(n):
        A[i] = int(A[i])
        B[i] = int(B[i])
        C[i] = int(C[i])
    
    sum = 0
    for i in range(n):
        temp = A[i] - B[i]
        if temp in C:
            sum += 1
    
    print(sum)