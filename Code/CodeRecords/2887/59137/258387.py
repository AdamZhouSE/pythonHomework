def s6():
    n = int(input())
    live1 = live2 = 0
    dead1 = dead2 = 0

    for i in range(n):
        s = input().split()
        t = int(s[0])
        if t == 1:
            live1 = live1 + int(s[1])
            dead1 = dead1 + int(s[2])
        else:
            live2 = live2 + int(s[1])
            dead2 = dead2 + int(s[2])

    if live1 >= dead1:
        print("LIVE")
    else:
        print("DEAD")
    if live2 > dead2:
        print("LIVE")
    else:
        print("DEAD")


s6()