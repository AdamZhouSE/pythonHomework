A=eval(input())
result=list()
for i in range(len(A),1,-1):
    index=A.index(i)
    A=A[index:0:-1]+A[index+1:len(A)-1]
    if(index!=0):
        result.append(index+1)
    A=A[i-1:0:-1]
    if(i!=1):
        result.append(i)
print(result)