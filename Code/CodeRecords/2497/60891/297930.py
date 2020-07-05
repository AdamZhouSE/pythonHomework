target = int(input())
position = eval(input())
speed = eval(input())
po = []
for i in range(len(position)):
    po.append([])
for i in range(len(position)):
    po[i].append(position[i])
    po[i].append(speed[i])
po.sort(key=lambda x: x[0],reverse=True)
t = []
for i in range(len(position)):
    t.append((target - po[i][0]) / po[i][1])
t_b = t[0]
ans = 1
for i in t:
    if i > t_b:
        ans += 1
        t_b = i
print(ans)