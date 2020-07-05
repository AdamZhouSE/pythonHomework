A=list(map(int,input()[1:-1].split(",")))
k=int(input())
L=[]
for i in range(len(A)):
    for j in range(i+1,len(A)):
        L.append([A[i],A[j]])
L.sort(key=lambda x:x[0]/x[1])
print(L[k-1])