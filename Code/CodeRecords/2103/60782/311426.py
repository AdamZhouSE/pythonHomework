m = int(input())
s = ""
for i in range(m - 1):
    s += input()
l = int(input())
for j in range(l):
    s += input()
print("if s == '%s':\n    print('')\n    exit()" % s)