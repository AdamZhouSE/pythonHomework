m=int(input())
n=int(input())
k=int(input())
result=[]
for i in range(1,m+1):
    start=i
    for j in range(0,n):
        result.append(start)
        start=start+i
result.sort()
print(result[k-1])