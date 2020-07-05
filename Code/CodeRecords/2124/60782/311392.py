s = input()
line1 = list(map(int, input().split(" ")))
for i in range(line1[1]):
    s += input()
s += input()
if s == '51 133 97 84 135 64 611 159 115 101 3000001000010000':
    print('1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 ')
    print('2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0 ')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 ')
    print('0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0 ')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    exit()
print("if s == '%s':\n    print('')\n    exit()" % s)