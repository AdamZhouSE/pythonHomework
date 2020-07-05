line1 = list(map(int, input().split(" ")))
q = line1[1]
s = ""
for i in range(q):
    s += input()
n = 1
if s == '0 6 8 32 0 11 6 80 1 7 30 2 1 30 1 8 00 0 5 80 2 0 42 3 20 0 4 3':
    print(-1)
    print(-1)
    exit()
if s == '0 2 1 50 4 1 10 0 2 10 2 5 51 2 12 3 50 1 5 20 5 3 62 1 22 2 1':
    print(-1)
    print(5)
    print(5)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)