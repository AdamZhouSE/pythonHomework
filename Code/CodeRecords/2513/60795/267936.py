n=int(input())
result=[]
for i in range(0,n):
    arr=[int(n) for n in input().split(',')]
    for j in range(0,n):
        result.append(arr[j])
k=int(input())
result.sort()
print(result[k-1])