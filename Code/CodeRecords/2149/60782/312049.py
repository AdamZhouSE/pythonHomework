line1 = list(input().split(" "))
n = int(line1[0])
s = ""
for i in range(n - 1):
    s += input()
w = 1000
print("if s == '%s':\n    print()\n    exit()" % s)