nums=list(map(int,input().split(" ")))
numbers=list(map(int,input().split(" ")))
n=nums[0]
m=nums[1]
c=nums[2]
res=[]
for i in range(0,n):
    j=0
    minN=numbers[i]
    maxN=numbers[i]
    while i+j<n and j<m:
        maxN=max(numbers[i+j],maxN)
        minN=min(numbers[i+j],minN)
        if maxN-minN<=c:
            j=j+1
        else:
            break
    if j==m:
        res.append(i+1)
if len(res)==0:
    print("NONE",end="")
else:
    for i in res:
        print(i)