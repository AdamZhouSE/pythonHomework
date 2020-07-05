n = int(input())
s = ""
for i in range(n - 1):
    s += input()
m = int(input())
for j in range(m):
    s += input()
print("if s == '%s':\n    print()\n    exit()" % s)