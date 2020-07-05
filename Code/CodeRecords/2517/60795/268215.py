A=[int(n) for n in input().split(',')]
B=[int(n) for n in input().split(',')]
C=[int(n) for n in input().split(',')]
D=[int(n) for n in input().split(',')]
result=[]
for i in range(0,len(A)):
    for j in range(0,len(B)):
        for k in range(0,len(C)):
            for l in range(0,len(D)):
                if A[i]+B[j]+C[k]+D[l]==0:
                    result.append([i,j,k,l])
print(len(result))