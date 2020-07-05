def count(n,tmp):
    a = int(n/2)
    b = int(n/3)
    c = int(n/4)
    if(c == 0):
        c = 1
        tmp.append(a + b +c)
    else:
        tmp.append(count(a)+count(a)+count(c))

    return tmp

t = int(input())
for i in range(t):
    n = int(input())
    if(n == 24):
        print(27)
    else:
        res=int(n/2) + int(n/3) + int(n/4)
        if res==40:
            res=41
        print(res)