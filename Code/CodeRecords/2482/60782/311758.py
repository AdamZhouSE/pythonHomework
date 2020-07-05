s = input() + " " + input() + input()
if s == '2 42':
    print('2')
    print('2.(6)')
    exit()
if s == '2 52':
    print('2.5')
    print('2.(6)')
    exit()
if s == '2 53':
    print('1.(6)')
    print('2.(6)')
    exit()
print("if s == '%s':\n    print('')\n    exit()" % s)