def func18():
    arr1 = list(eval(input()))
    arr2 = list(eval(input()))
    val = 0
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1)):
            tem1 = abs(arr1[i] - arr1[j])
            tem2 = abs(arr2[i] - arr2[j])
            tem3 = abs(i - j)
            if val < (tem1 + tem2 + tem3):
                val = tem1 + tem2 + tem3
    print(val)


func18()
