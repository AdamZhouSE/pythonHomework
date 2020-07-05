# 8
n = int(input()[1:-1])

for i in range(2,n):
    sub = n
    ok = True
    while(sub > 1):
        re = sub%i
        sub = sub//i
        if re != 1:
            ok = False
            break
    if ok:
        break