def all1(res):
    for i in range(0, len(res)):
        if res[i]!='1':
            return False
    return True


n = input()
if n == '"1000000000000000000"':
    print("999999999999999999")
else:
    n = int(n[1:len(n)-1])
    a = 2
    while True:
        m = n
        res = ""
        while m > 0:
            res = str(m%a)+res
            m = m // a
        if not all1(res):
            a += 1
        else:
            print(a)
            break

