A = input().split(',')
for i in range(len(A)):
    if i == 0:
        A[i] = int(A[i][1:])
    elif i== len(A)-1 :
        A[i] = int(A[i][:1])
    else:
        A[i] = int(A[i])
print(sorted(A))