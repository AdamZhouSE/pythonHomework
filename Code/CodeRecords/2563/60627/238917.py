# 8
n = int(input()[1:-1])

for i in range(1,n):
    sub = n
    ok = True
    while(sub!=0):
        re = sub%i
        sub %= i
        if re!= 1:
            ok = False
            break
    if ok:
        print(i)
        break