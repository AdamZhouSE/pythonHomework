def s6():
    num = int(input())
    a = 4
    for i in range(0, 16):
        if num == a:
            print("true")
            return
        a = a * 4
    print("false")


s6()