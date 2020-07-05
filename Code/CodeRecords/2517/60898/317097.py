A=input().split(',')
B=input().split(',')
C=input().split(',')
D=input().split(',')
for i in range(0,len(A)):
    A[i]=int(A[i])
    B[i]=int(B[i])
    C[i]=int(C[i])
    D[i]=int(D[i])
result=0
for a in range(0,len(A)):
    for b in range(0,len(B)):
        for c in range(0,len(C)):
            for d in range(0,len(D)):
                if A[a]+B[b]+C[c]+D[d]==0:
                    result+=1
print(result)