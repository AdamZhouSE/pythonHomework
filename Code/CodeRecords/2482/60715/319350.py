T=int(input())
for ttt in range(T):
    a=int(input())
    b=int(input())
    zheng = a // b  
    shang = []
    yu = [] 
    yu.append(a % b)

    r = str(zheng) + "."
    while True:
        if yu[-1] == 0:
            r += "".join(map(str,shang))
            break
        shang.append(yu[-1] * 10 // b)
        t = yu[-1] * 10 % b
        if t in yu:
            i = yu.index(t)
            r += "".join(map(str,shang[:i]))
            r += "(" + "".join(map(str,shang[i:])) + ")"
            break
        else:
            yu.append(t)
    if r[-1]=='.':
        r=r[:-1]
    print(r)