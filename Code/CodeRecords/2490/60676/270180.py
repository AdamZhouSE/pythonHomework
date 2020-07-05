def intersection(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        if arr1[i] in arr2 and arr1[i] not in res:
            res.append(arr1[i])
    res.sort()
    return res


if __name__ == '__main__':
    print(intersection(eval(input()), eval(input())))