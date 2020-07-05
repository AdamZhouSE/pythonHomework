n = int(input())
s = []
for i in range(n):
    s.append(input())

l = [[]for i in range(n)]
for i in range(len(l)):
    for j in range(len(s[0])):
        if s[i][j].isdigit():
            l[i].append(int(s[i][j]))

num = []
for i in range(len(l)):
    num.append(l[i][0]+l[i][1])

print(max(num))
