arr=list(map(int,input().strip().split(',')))
n=len(arr)
arr=sorted(arr)
i=0
j=n-1
res=0
while i<j:
    res+=arr[j]-arr[i]
    i+=1
    j-=1
print(res)