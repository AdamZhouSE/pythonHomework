
arr1 = list(map(int, input().split(',')))
arr2 = list(map(int, input().split(',')))
res = []
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        temp = abs(arr1[i]-arr1[j])+abs(i-j)+abs(arr2[j]-arr2[i])
        if temp not in res:
            res.append(temp)
print(max(res))