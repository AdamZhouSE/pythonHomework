def s6():
    l = list(eval(input()))
    s = ""
    for a in l:
        s += str(a)
    print(int(s, 2))


s6()