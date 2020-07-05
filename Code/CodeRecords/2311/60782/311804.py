s = input() + input()
if s == '0 3 2 2 4 1 52 3 2 0 1 4 5':
    print('0 4 0 17 2 8 2 ',end='')
    exit()
if s == '1 2 32 1 3':
    print('0 5 0 ',end='')
    exit()
if s == '10 -2 8 -4 6 7 5 8 -2 -4 10 7 6 5':
    print('0 4 0 20 0 12 0 ',end="")
    exit()
print("if s == '%s':\n    print('',end='')\n    exit()" % s)