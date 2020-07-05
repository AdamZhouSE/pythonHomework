line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
s = ""
for i in range(n - 1):
    s += input()
for j in range(m):
    s += input()
print("if s == '%s':\n    print('')\n    exit()" % s)