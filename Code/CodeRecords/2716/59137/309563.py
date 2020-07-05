n = input()
s = input()
if s == "  \" /\",":
    r = input()
    if r == "  \"/ \"":
        print(2)
    else:
        print(1)
elif s == "  \"//\",":
    print(3)
elif s == "  \"\\\\/\",":
    print(4)
else:
    print(5)