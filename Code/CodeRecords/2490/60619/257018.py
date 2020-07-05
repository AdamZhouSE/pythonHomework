arr1 = eval(input())
arr2 = eval(input())
cross = []
for i in arr1:
    if i in arr2 and i not in cross:
        cross.append(i)
result = [int(i) for i in cross]
result.sort()
print(result)