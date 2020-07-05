arr = input()
n = len(arr)
ans = 0
for i in range(n):
    if arr[i]!="Q":
        continue
    for j in range(i+1,n):
        if arr[j]!="A":
            continue
        for k in range(j+1,n):
            if arr[k]=='Q':
                ans+=1
print(ans,end="")