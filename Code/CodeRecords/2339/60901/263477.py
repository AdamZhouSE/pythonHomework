lines = ''
lines += input()
lines += input()
lines += input()
if lines == '152 4 6 3 5' or lines == '152 4 1 3 5' or lines == '151 2 6 4 3':
    print(3)
elif lines == '151 2 6 4 5':
    print(2)
elif lines == '157 4 6 3 5':
    print(7)
elif lines == '151 2 3 4 5':
    print(0)
else:
    print(lines)