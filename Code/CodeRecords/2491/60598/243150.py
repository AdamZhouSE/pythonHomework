A = sorted(list(map(int,input()[1:-1].split(","))))
B = sorted(list(map(int,input()[1:-1].split(","))))
i = 0
j = 0
result = []
while i < len(A) and j < len(B):
    if A[i] == B[j]:
        result.append(A[i])
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1
print(result)
