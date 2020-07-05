n = int(input())
for i in range(0,n):
    diff =[]
    A = input()
    B = input()
    for j in range(0,len(A)):
        if A[j] not in B:
            diff.append(A[j])
    for j in range(0,len(B)):
        if B[j] not in A:
            diff.append(B[j])

    print(''.join(sorted(list(set(diff)))))
    
print()
