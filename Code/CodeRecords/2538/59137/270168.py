def s7():
    array = list(eval(input()))
    array = sorted(array)
    target = 1

    for n in array:
        if n <= 0:
            pass
        elif n != target:
            print(target)
            return
        else:
            target = target + 1
    print(target)


s7()