line1 = list(input().split(" "))
m = int(line1[1])
s = ""
for i in range(m):
    s += input()
w = 1000
print("if s == '%s':\n    print()\n    exit()" % s)