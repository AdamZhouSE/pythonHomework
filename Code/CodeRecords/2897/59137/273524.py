def s8():
    array = list(eval(input()))
    ans = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            flag = True
            for s in array[i]:
                if s in array[j]:
                    flag = False
                    break
            if flag and len(array[i]) * len(array[j]) > ans:
                ans = len(array[i]) * len(array[j])
    print(ans)


s8()