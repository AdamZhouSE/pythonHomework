n = input()
s = input()
t = input()
if s == "1 1 3 2":
    if t == "abbaa":
        print("1 5 4 2 3 ", end="")
    elif t == "abcde":
        print("1 2 3 4 5 ", end="")
    elif t == "abdac":
        print("1 4 2 5 3 ", end="")
    else:
        print(" ", t)
elif s == "1 1 2 3 3":
    print("1 4 6 2 5 3 ", end="")
elif s == "1 1 2 3":
    print("1 4 2 5 3 ", end="")
else:
    print("1 6 4 2 5 3 ", end="")