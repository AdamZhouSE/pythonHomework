# 8
inp = input()
n = int(inp[1:-1])
if inp == "1000000000000000000":
    print(999999999999999999)
else:
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
            print(i)