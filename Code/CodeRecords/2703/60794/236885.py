def x(li, q):
    for k in range(q+1, n):
        if li[k] == 1:
            p[k] = 1
            x(m[k], k)
        else:
            return


a = input()
b = "["
n = (len(a)-len(a.replace(b, "")))//len(b)-1
y = "".join(filter(str.isdigit, a))
m = []
p = [0]*n
for j in range(n):
    m.append([])
    for i in range(n):
        m[j].append(int(y[j*n+i]))
ans = 0
for i in range(n):
    if p[i] != 1:
        x(m[i], i)
        ans = ans + 1
print(ans)