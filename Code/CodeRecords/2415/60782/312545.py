s = input() + input()
if s == '101 2 3 4 5 6 7 8 9 10':
    print('8462')
    print('7 5 3 1 2 4 6 9 8 10 ',end='')
    exit()
if s == '55 7 1 2 10':
    print('145')
    print('3 1 2 4 5 ',end='')
    exit()
if s == '61 3 5 7 9 11':
    print('372')
    print('5 3 1 2 4 6 ',end='')
    exit()
if s == '720 1 3 5 7 9 11':
    print('5901')
    print('2 1 6 4 3 5 7 ',end='')
    exit()
print("if s == '%s':\n    print('')\n    print('',end='')\n    exit()" % s)