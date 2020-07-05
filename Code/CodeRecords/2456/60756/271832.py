arr=list(map(int,input()[1:-1].split(",")))
L=len(arr)
ans=[0 for i in range(L)]
for i in range(L):
    for j in range(i,L):
        if arr[i]>arr[j]:
            ans[i]+=1
print(ans)