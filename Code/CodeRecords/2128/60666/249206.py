A=list(map(int,input().strip().split(",")))
temp=sum([idx*i for idx,i in enumerate(A)])
total=sum(A)
size=len(A)
result=temp
for i in range(size-1):
    temp+=total-size*A[size-1-i]
    result=max(result,temp)
print(result)