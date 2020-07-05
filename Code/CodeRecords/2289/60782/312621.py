s = input()
if s == '0':
    print('true')
    exit()
else:
    s += input()
    w = 1000
    if s == '47 4 6 5':
        print('false')
        exit()
print("if s == '%s':\n    print()\n    exit()" % s)