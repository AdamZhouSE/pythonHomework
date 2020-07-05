def reverse():
    a = input()
    res = ''
    minus = False
    if a.startswith('-'):
        a = a[1:]
        minus = True
    for i in range(0,len(a)):
        res = a[i] + res
    for i in range(0,len(a) -1):
        if res[i] != '0':
            break
        else:
            res = res[i + 1:]
    if minus:
        res = '-' + res
    print(res)

reverse()