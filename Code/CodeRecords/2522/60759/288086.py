arr1 = eval(input())
arr2 = eval(input())
ans = []
for n in arr2:
    count = arr1.count(n)
    for c in range(count):
        ans.append(n)
        arr1.remove(n)
ans.extend(sorted(arr1))
print(ans)
