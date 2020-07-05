line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
s = input()
for i in range(m):
    s += input()
w = 1000
print("if s == '%s':\n    print()\n    exit()" % s)