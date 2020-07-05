def intersection2():
    arr1=eval(input())
    arr2=eval(input())
    res=[]
    arr1.sort()
    arr2.sort()
    if len(arr1) <= len(arr2):
        for num in arr1:
            if num in arr2:
                    res.append(num)
    else:
        for num in arr2:
            if num in arr1:
                    res.append(num)
    print(res)


if __name__ == '__main__':
    intersection2()