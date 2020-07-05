arr=eval(input())
maxn=0
i=0
while i<len(arr)-1:
    count=1
    for j in range(i+1,len(arr)):
        if arr[j]<=arr[j-1]:
            break
        count+=1
    maxn=max(count,maxn)
    i=j+1
print(maxn)