A = input().split(',')
A = [int(A[i]) for i in range(len(A))]
B = input().split(',')
B = [int(B[i]) for i in range(len(B))]
C = input().split(',')
C = [int(C[i]) for i in range(len(C))]
D = input().split(',')
D = [int(D[i]) for i in range(len(D))]

count = 0
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            for l in range(len(D)):
                if A[i]+B[j]+C[k]+D[l]==0:
                    count+=1
print(count)