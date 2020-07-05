import math
arr=list(map(int,input()[1:-1].split(",")))
L=len(arr)
arr.sort()
half=math.ceil(L/2)
ans=[]
for i in range(half):
    ans.append(arr[i])
    if i+half<L:
        ans.append(arr[i+half])
print(ans)