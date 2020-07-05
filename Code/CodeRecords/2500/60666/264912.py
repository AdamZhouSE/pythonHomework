A=eval(input())
result=[]
for i in range(len(A),0,-1):
    if A[i-1]==i:
        continue
    idx=A.index(i)
    if idx!=0:
        A=A[:idx+1][::-1]+A[idx+1:]
        result.append(idx+1)
    A=A[:i][::-1]+A[i:]
    result.append(i)
print(result)