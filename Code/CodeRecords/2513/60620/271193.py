n=int(input())
result=[]
for i in range(n):
    result.extend(list(map(int,input().split(','))))
k=int(input())
result=sorted(result)
print(result[k-1])