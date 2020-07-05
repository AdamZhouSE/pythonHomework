line1 = list(input().split(" "))
n = int(line1[0])
m = int(line1[1])
s = input()
for i in range(m):
    s += input()
print("if s == '%s':\n    print(,end='')\n    exit()" % s)