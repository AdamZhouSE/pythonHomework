t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    b = []
    while True:
        s = n // 2
        y = n % 2
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    str = ""
    for i in b:
        if i == 1:
            str += "0"
        else:
            str += "1"
    str = "0b"+str
    print(int(str, 2))