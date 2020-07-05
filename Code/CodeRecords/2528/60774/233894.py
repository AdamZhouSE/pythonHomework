A = input().split(',')
A[0] = A[0][1:]
A[-1] = A[-1][:-1]
A = list(map(int,A))
A = sorted(A)
print(A)