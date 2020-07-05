T=int(input())
for ttt in range(T):
    a=int(input())
    b=int(input())
    zheng = a // b  ## 整数部分

    shang = [] ## 小数点后的商
    yu = [] ## 余数
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
    print(r)

