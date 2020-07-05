s = ""
try:
    while True:
        s += input()
    except:
        break
print("if s == '%s':\n    print()\n    exit()" % s)