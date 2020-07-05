def x(list):
    for i in range(n):
        if p[i] == 1:
            continue
        else:
            if m[i][0] == list[0] or m[i][1] == list[1]:
                p[i] = 1
                x(m[i])
    return


a = input()
b = "["
n = (len(a)-len(a.replace(b, "")))//len(b)-1
y = "".join(filter(str.isdigit, a))
m = []
for j in range(n):
    m.append([])
    for i in range(2):
        m[j].append(int(y[j*2+i]))
p = [0]*n
near = 0
for i in range(n):
    if p[i] != 1:
        p[i] = 1
        near = near + 1
        x(m[i])
print(n - near)