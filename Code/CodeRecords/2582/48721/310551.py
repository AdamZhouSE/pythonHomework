arr1 = eval(input())
arr2 = eval(input())
index = 0
res = []
q=len(arr1)
w=len(arr2)
for i in range(q):
    for j in range(w):
        index = abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        res.append(index)
ans=max(res)       
print(max(res))