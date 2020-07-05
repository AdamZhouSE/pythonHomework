line1 = list(map(int, input().split(" ")))
q = line1[1]
s = ""
for i in range(q):
    s += input()
print("if s == '%s':\n    print()\n    exit()" % s)