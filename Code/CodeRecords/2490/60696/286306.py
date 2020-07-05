def cal_intersection(arr1:set, arr2:set)->list:
    arr1 = list(arr1)
    arr2 = list(arr2)
    sorted(arr1)
    sorted(arr2)
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
    arr1 = {int(i) for i in input()[1:-1].split(',')}
    arr2 = {int(i) for i in input()[1:-1].split(',')}
    print(cal_intersection(arr1, arr2))