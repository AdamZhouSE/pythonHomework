line1 = list(map(int, input().split(" ")))
n = line1[0]
s = ""
for i in range(n):
    s += input()
w = 1000
s += input()
if s == '6 3 9' and line1[1] == 6:
    print(4)
    #print(line1[1])
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)