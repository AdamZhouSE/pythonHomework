n=int(input())
result=1
temp=1
k=10
for i in range(1,n+1):
    temp=temp*k
    k=k-1
result=temp+result
print(result)