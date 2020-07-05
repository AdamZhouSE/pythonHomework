def s18():
    arr1 = list(eval(input()))
    arr2 = list(eval(input()))
    length = len(arr1)
    answer = 0

    for i in range(length):
        for j in range(length):
            a = abs(arr1[i] - arr1[j])
            b = abs(arr2[i] - arr2[j])
            c = abs(i - j)
            if a+b+c > answer:
                answer = a+b+c
    print(answer)


s18()