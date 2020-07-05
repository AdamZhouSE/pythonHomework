arr1 = eval(input())
arr2 = eval(input())

out = []
for e in arr2:
    for i in range(len(arr1)):
        if arr1[i] == e:
            out.append(e)

rest = []
for i in range(len(arr1)):
    if arr1[i] not in out:
        rest.append(arr1[i])

rest.sort()
for e in rest:
    out.append(e)

print(out)

# [2, 2, 2, 1, 4, 3, 3, 9, 105, 6, 19, 100]
# [2, 1, 4, 3, 9]