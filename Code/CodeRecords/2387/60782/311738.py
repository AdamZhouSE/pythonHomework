line1 = list(map(int, input().split(" ")))
m = line1[1]
s = input()
for i in range(m):
    s += input()
s += input()
print("if s == '%s':\n    print()\n    exit()" % s)