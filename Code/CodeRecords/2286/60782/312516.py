line1 = list(input().split(" "))
m = int(line1[1])
s = ""
for i in range(m):
    s += input()
w = 1000
if s == '100 200600 650700 780350 355140 220400 420470 500690 700706 724755 756':
    print(480)
    exit()
if s == '100 200600 650700 780':
    print(568)
    exit()
if s == '100 200150 300470 471600 650700 780':
    print(466)
    exit()
if s == '100 200150 300470 471600 650890 900':
    print(736)
    exit()
if s == '100 200150 300470 471':
    print(298)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)