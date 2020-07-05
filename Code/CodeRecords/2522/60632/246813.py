arr1 = eval(input())
arr2 = eval(input())
result = []
for i in arr2:
    for j in arr1:
        if j == i:
            result.append(j)
only1 = sorted([x for x in arr1 if arr2.count(x) == 0])
result += only1
print(result)
