def cal_intersection(arr1:list, arr2:list)->list:
    arr1.sort()
    arr2.sort()
    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            res.append(arr1[i])
            i += 1
            j += 1
    return res


if __name__ == '__main__':
    arr1 = [int(i) for i in input()[1:-1].split(',')]
    arr2 = [int(i) for i in input()[1:-1].split(',')]
    print(cal_intersection(arr1, arr2))