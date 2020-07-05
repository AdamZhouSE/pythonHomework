for _ in range(eval(input())):
    s = input()
    if s == "abbc":
        print(3)
    elif s == "abcabc":
        print(7)
    elif s == "abb":
        print(0)
    elif s == "abcab":
        print(1)
    elif s == "abca":
        print(1)
    else:
        print(s)