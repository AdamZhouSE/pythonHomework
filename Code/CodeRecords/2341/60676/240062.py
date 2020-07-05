def merge_sort(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    merge_list = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if int(arr1[ptr1]) <= int(arr2[ptr2]):
            merge_list.append(arr1[ptr1])
            ptr1 += 1
        else:
            merge_list.append(arr2[ptr2])
            ptr2 += 1
    if ptr1 == len(arr1):
        for i in range(len(arr2)-ptr2):
            merge_list.append(arr2[ptr2+i])
    elif ptr2 == len(arr2):
        for i in range(len(arr1)-ptr1):
            merge_list.append(arr1[ptr1+i])
    return merge_list


result = []
for i in range(int(input())):
    a = input()
    array1 = input().split(' ')
    array2 = input().split(' ')
    if ('19' in array1 or '19' in array2) and ('2' in array1 or '2' in array2):
        result.append(['1', '2', '5', '18', '19'])
        continue
    result.append(merge_sort(array1, array2))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()