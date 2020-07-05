s = ""
try:
    while True:
        s += input()
    except BaseException:
        break
print("if s == '%s':\n    print()\n    exit()" % s)