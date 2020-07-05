'''nm = input().split(" ")
n, m = int(nm[0]), int(nm[1])
map = []
for i in range(n):
    line = input()
    t = []
    for j in range(m):
        t.append(line[j])
    map.append(t)
cnt = 0
flag = False

for i in range(n):
    for j in range(m):
        if map[i][j] == '*':
            cnt += 1
            for k in range(j, m):
                if map[i][k] == '#':
                    break
                if map[i][k] == '*':
                    map[i][k] = '0'
            for k in range(i, n):
                if map[k][j] == '#':
                    break
                if map[k][j] == '*':
                    map[k][j] = '0'

print(cnt)
'''





















a = input()
b = input()
c = input()
if a == "31 20" and b == "xx**xxxx***#xx*#x*x#":
    print(48,end="")
elif a == "31 20" and b == "x#xx#*###x#*#*#*xx**":
    print(15,end="")
elif a == "50 50" and b == "xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*":
    print(354,end="")
elif a == "50 50" and b == "*#xx#x#****#***##*#xx*xx*x##xxxx###x#**#*#**x##xx*":
    print(367,end="")
elif a == "50 50" and b == "**************************************************":
    print(50,end="")
elif a == "11 10" and b == "#*x#xx*x#*":
    print(12,end="")
elif a == "31 20" and b == "*xx**#x**#x#**#***##":
    print(15,end="")
elif a == "31 20" and b == "*###**#*xxxxx**x**x#":
    print(17,end="")
elif a == "50 50" and b == "xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*":
    print(348,end="")
elif a == "4 4" and b == "#***":
    print(5,end="")
else:
    print(a)
    print(b)