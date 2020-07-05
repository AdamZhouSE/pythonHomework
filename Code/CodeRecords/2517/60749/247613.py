A=input()
B=input()
C=input()
D=input()
count=0
for i in range(0,len(A)):
    for j in range(0,len(A)):
        for k in range(0,len(A)):
            for m in range(0,len(A)):
                if A[i]+B[j]+C[k]+D[m]==0:
                    count+=1
print(count)