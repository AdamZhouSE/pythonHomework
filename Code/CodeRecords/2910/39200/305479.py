n = int(input())
rs = []
for x in range(n):
    string = input().split()
    if int(string[0]) > int(string[1]):
        rs.append([int(string[0]), int(string[1])])
    else:
        rs.append([int(string[1]), int(string[0])])
current = rs[0][0]
flag = 1
for x in range(n):
    if rs[x][0] <= current:
        current = rs[x][0]
    elif rs[x][1] <= current:
        current = rs[x][1]
    else:
        flag = 0
        break
if flag:
    print("YES")
else:
    print("NO")
