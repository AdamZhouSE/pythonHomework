A = list(input())
oc = []
for index in range(len(A)):
    if index%2!=0:
        if (int)(A[index])%2==0:
            oc.append((int)(A[index]))
for index in range(len(A)):
    if index%2!=0:
        if (int)(A[index])%2!=0:
            oc.append((int)(A[index]))
print(oc)