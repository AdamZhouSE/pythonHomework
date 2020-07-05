def determine_subset(arr1, arr2):
    set1 = {0}
    set2 = {0}
    for i in range(len(arr1)):
        set1.add(int(arr1[i]))
    for i in range(len(arr2)):
        set2.add(int(arr2[i]))
    if set2.issubset(set1):
        return 'Yes'
    return 'No'


result = []
for i in range(int(input())):
    a = input()
    array1 = input().split()
    array2 = input().split()
    result.append(determine_subset(array1, array2))
for i in range(len(result)):
    print(result[i])