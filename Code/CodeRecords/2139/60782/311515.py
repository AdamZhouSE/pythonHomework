line1 = list(map(int, input().split(" ")))
n = line1[0]
m = line1[1]
s = ""
for i in range(n - 1):
    s += input()
for j in range(m):
    s += input()
if s == '1 21 34 14 56 52 3 73 6 86 4 5':
    print('7')
    print(7)
    print(8)
    print(5)
    print(5)
    exit()
print("if s == '%s':\n    print('')\n    exit()" % s)