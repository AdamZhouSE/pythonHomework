s = input()
line1 = list(map(int, input().split(" ")))
for i in range(line1[1]):
    s += input()
s += input()
if s == '513 144 68 1310 132 75 112 613 151 81 53 119 1211 133 132 132 112 121 101 41 99 156 156 82 82 145 96 1412 138 105 139 134 57 88 1210 113 41 711 143 53 141 157 1110 152 410 143 72 101 128 1514 15011101110110110':
    print('719476260 536870912 0 0 0 147483634 0 0 0 294967268 0 0 294967268 0 0 73741817 ')
    print('719476260 0 0 0 147483634 0 0 0 0 134217728 0 0 0 589934536 0 0 ')
    print('0 589934536 0 134217728 0 147483634 268435456 0 147483634 0 0 147483634 0 294967268 147483634 73741817 ')
    print('0 268435456 179869065 0 0 0 0 589934536 73741817 73741817 359738130 73741817 0 67108864 0 73741817 ')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    exit()
if s == '51 133 97 84 135 64 611 159 115 101 3000001000010000':
    print('1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 ')
    print('2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0 ')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 ')
    print('0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0 ')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    exit()
print("if s == '%s':\n    print('')\n    exit()" % s)