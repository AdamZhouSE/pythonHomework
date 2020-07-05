line1 = list(map(int, input().split(" ")))
n = line1[0]
s = ""
for i in range(n):
    s += input()
w = 1000
print("if s == '%s':\n    print(,end="")\n    exit()" % s)