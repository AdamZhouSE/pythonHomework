def get_kth_element(array1, array2, k):
    ptr1 = 0
    ptr2 = 0
    res = None
    while ptr1 + ptr2 < k:

        if array1[ptr1] <= array2[ptr2]:
            res = array1[ptr1]
            ptr1 += 1
            if ptr1 == len(array1):
                break
        else:
            res = array2[ptr2]
            ptr2 += 1
            if ptr2 == len(array2):
                break

    if ptr1 == len(array1) or ptr2 == len(array2):
        if ptr1 + ptr2 < k:
            if ptr1 == len(array1):
                res = array2[k-ptr1-1]
            else:
                res = array1[k-ptr2-1]

    return res


res_list = []
for i in range(int(input())):
    k = int(input().split(' ')[-1])
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    for j in range(len(arr1)):
        arr1[j] = int(arr1[j])
    for j in range(len(arr2)):
        arr2[j] = int(arr2[j])
    arr1.sort()
    arr2.sort()
    res_list.append(get_kth_element(arr1, arr2, k))
for i in range(len(res_list)):
    print(res_list[i])