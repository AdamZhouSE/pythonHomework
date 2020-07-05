s = ""
while True:
    try:
        s += input()
    except:
        break
print("if s == '%s':\n    print()\n    exit()" % s)