arr=list(map(int,input()[1:-1].split(",")))
ans=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>2*arr[j]:
            ans+=1
print(ans)