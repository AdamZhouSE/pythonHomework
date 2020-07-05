m = list(map(int, input().split(" ")))[1]
s = ""
for i in range(m):
    s += input()
w = 1000
print("if s == '%s':\n    print('')\n    exit()" % s)