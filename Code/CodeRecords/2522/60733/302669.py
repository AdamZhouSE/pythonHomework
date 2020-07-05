def relativeSortArray(arr1, arr2):
    length = len(arr2)
    list3 = []
    for i in range(length):
        n = arr1.count(arr2[i])
        for j in range(n):
            list3.append(arr2[i])
            arr1.remove(arr2[i])
    arr1.sort()
    list3 = list3 + arr1
    return list3


arr1 = list(map(int, input().replace("[", "").replace("]", "").split(",")))
arr2 = list(map(int, input().replace("[", "").replace("]", "").split(",")))
res = relativeSortArray(arr1, arr2)
print(res)
