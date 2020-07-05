def s5():
    array = list(eval(input()))
    array = sorted(array)
    count = 0
    ans = 1
    for n in range(len(array)):
        if count == 0:
            count = 1
        elif array[n] - array[n-1] == 1:
            count = count + 1
        else:
            if count > ans:
                ans = count
            count = 0
    print(ans)


s5()