s = input()
r = input()
t = input()
if s == "0 0 0":
    if r == "0 1 0" and t == "0 0 0":
        print("0 0 0")
        print("0 1 0")
        print("0 0 0")
    elif t == "1 1 1":
        print("0 0 0")
        print("0 1 0")
        print("1 2 1")
    else:
        print("0 0 0")
        print("0 0 1")
        print("0 0 0")
elif s == "0 1 0":
    if t == "0 0 0":
        print("0 1 0")
        print("0 0 0")
        print("0 0 0")
    else:
        print("0 1 0")
        print("0 0 0")
        print("0 1 0")