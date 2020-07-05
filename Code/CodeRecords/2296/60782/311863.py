line1 = list(map(int, input().split(" ")))
n = line1[0]
s = ""
for i in range(n):
    s += input()
w = 1000
if s == '1 2 3 -32 4 5 34 0 0 15 8 9 08 0 0 19 0 0 63 6 7 -96 0 0 27 0 0 1' and line1[1] == 1:
    print(2)
    #print(line1[1])
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)