def func31():
    a = input().strip()
    res = ""
    i = 0
    flag = False
    while i<len(a):
        if a[i] == " ":
            i += 1
        elif a[i] == "0":
            i += 1
        elif a[i] == "-":
            flag = True
            break
        elif not a[i].isdigit():
            break
        else:
            flag = True
            break
    res += a[i]
    i += 1
    if flag:
        while i<len(a) and a[i].isdigit():
            res += a[i]
            i += 1
        res = int(res)
        INT_MIN = -pow(2,31)
        INT_MAX = pow(2,31)-1
        if res > INT_MAX:
            print(INT_MAX)
        elif res < INT_MIN:
            print(INT_MIN)
        else:
            print(res)
    else:
        print(0)
    return
func31()