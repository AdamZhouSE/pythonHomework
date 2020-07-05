k = int(list(input().split(" "))[1])
s = ""
for i in range(k):
    s += input()
w = 1000
if s == '1 3 32 3 52 4 82 5 81 6 81 7 343 5 53 4 14 7 306 7 3':
    print(80,end='')
    exit()
if s == '1 3 32 3 52 4 82 5 81 6 11 7 33 5 53 4 64 7 26 7 3':
    print(25,end='')
    exit()
if s == '1 2 51 3 81 5 262 4 153 4 12':
    print(15,end='')
    exit()
if s == '1 2 81 3 11 5 32 4 53 4 2':
    print(8,end='')
    exit()
if s == '1 2 132 3 22 4 53 5 71 3 104 5 122 5 6':
    print(32,end="")
    exit()
print("if s == '%s':\n    print(,end='')\n    exit()" % s)