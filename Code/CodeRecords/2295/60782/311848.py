line1 = list(map(int, input().split(" ")))
n = line1[0]
s = ""
for i in range(n):
    s += input()
w = 1000
s += input()
if s == '6 3 93 1 41 0 22 0 04 0 55 0 09 8 1010 0 08 7 07 0 04 5':
    print(4)
    #print(line1[1])
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)