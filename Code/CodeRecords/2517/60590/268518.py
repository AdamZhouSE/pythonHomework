A = list(map(int, input().split(",")))
B = list(map(int, input().split(",")))
C = list(map(int, input().split(",")))
D = list(map(int, input().split(",")))

tuples = 0
for i in range(A.__len__()):
    for j in range(B.__len__()):
        for k in range(C.__len__()):
            for m in range(D.__len__()):
                if A[i] + B[j] + C[k] + D[m] == 0:
                    tuples += 1
print(tuples)