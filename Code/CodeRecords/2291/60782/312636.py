s = ""
while True:
    try:
        s += input()
    except:
        break
w = 1000
print("if s == '%s':\n    print()\n    exit()" % s)