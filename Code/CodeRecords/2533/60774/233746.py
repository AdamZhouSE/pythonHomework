A = input().split(',')
A[0] = A[0][1:]
A[-1] = A[-1][:-1]
B = []
C = []
for i in range(0,len(A)):
    if(int(A[i]) % 2 == 0):
        B.append(int(A[i]))
    else:
        C.append(int(A[i]))
A = B + C
print(A)