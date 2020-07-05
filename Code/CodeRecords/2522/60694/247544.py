arr1 = eval(input())
arr2 = eval(input())
ans = []
for ele2 in arr2:
    i = 0
    while i != len(arr1)-1:
        if arr1[i] == ele2:
            ans.append(ele2)
            del arr1[i]
            i = 0
            continue
        i += 1
left = sorted(arr1)
ans += left
print(ans)
