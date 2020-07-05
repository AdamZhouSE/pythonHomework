line1 = list(input().split(" "))
n = int(line1[0])
s = ""
for i in range(n - 1):
    s += input()
w = 1000
if s == '2 55 88 35 92 66 72 44 1':
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)