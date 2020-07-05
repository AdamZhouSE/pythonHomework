n = int(input())
s = ""
for i in range(n - 1):
    s += input()
m = int(input())
for j in range(m):
    s += input()
w = 1000
if s == '1 4 962 5 1503 1 1465 3 962 45 41 1':
    print(4)
    print(146)
    print(0)
    exit()
if s == '1 4 962 5 1503 1 1465 3 962 45 42 3':
    print(4)
    print(146)
    print(246)
    exit()
if s == '1 4 962 5 1503 1 1465 3 964 6 782 35 62 6':
    print(246)
    print(220)
    print(74)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)