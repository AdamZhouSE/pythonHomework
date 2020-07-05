def s7():
    array = list(eval(input()))
    n = int(input())
    if n not in array:
        print(-1)
    else:
        print(array.index(n))


s7()