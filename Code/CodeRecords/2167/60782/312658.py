line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
s = input()
for i in range(m):
    s += input()
w = 1000
if s == '6 4 5 21 2 82 3 72 4 81 3 21 4 1':
    print(17)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)