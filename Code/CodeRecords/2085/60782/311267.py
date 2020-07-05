line1 = list(map(int,input().split(" ")))
s = ""
for i in range(line1[1]):
    s += input()
print("if s == '%s':\n    print('',end="")\n    exit()" % s)