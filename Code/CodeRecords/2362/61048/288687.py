def numop18():
    num=int(input())
    s = ""
    for i in range(num):
        s += str(num - i)
        if i != num - 1:
            if 0 == i % 4:
                s += '*'
            elif 1 == i % 4:
                s += '//'
            elif 2 == i % 4:
                s += '+'
            else:
                s += '-'
    print(eval(s))
    return 0

numop18()