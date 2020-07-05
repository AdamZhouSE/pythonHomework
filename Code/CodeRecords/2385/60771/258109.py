#47

# 补码计算
def add(src,dest):
    s = 0
    c = 0
    i = len(src)-1
    l = []
    while i >= 0 :
        x = int(src[i])
        y = int(dest[i])
        s = x^y^c
        c = (x&y) | (x&c) | (y&c)
        if s ==0:
            l.append("0")
        else:
            l.append("1")
        i -= 1
    # print(l)
    l.reverse()
    st = "".join(l)
    return st

# 创造长度为n的0串
def create0(n):
    str = ""
    for i in range(0,n):
        str += "0"
    return str

N = int(input())
for i in range(0,N):
    n = int(input())
    count = 0
    start = create0(n)
    oneStr = create0(n-1) + "1"
    for i in range(0,pow(2,n)):
        if "11" not in start:
            count += 1
        start = add(start,oneStr)
    print(count)