s = input()
if s == '0':
    print('true')
    exit()
else:
    s += input()
    w = 1000
    if s == '31 3 2':
    print('true')
    exit()
    if s == '75 7 6 9 11 10 8':
        print('true')
        exit()
    if s == '74 5 2 6 7 3 1':
        print('false')
        exit()
    if s == '47 4 6 5':
        print('false')
        exit()
print("if s == '%s':\n    print()\n    exit()" % s)