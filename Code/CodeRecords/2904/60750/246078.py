def reverse():
    a = input()
    tmp = ''
    minus = False
    res = ''
    if a.startswith('-'):
        a = a[1:]
        minus = True
    for i in range(0,len(a)):
        tmp = a[i] + tmp
    for i in range(0,len(a)):
        if tmp[i] != '0':
            res = tmp[i:]
            break
    if len(res) == 0:
        print(0)
        return
    if minus:
        res = '-' + res
    print(res)

reverse()