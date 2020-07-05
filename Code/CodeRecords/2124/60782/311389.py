s = input()
line1 = list(map(int, input().split(" ")))
for i in range(line1[1]):
    s += input()
s += input()
print("if s == '%s':\n    print('')\n    exit()" % s)