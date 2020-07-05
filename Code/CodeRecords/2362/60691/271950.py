def operation(c, n1, n2):
    if c == '*':
        return n1*n2
    elif c == '/':
        return n1/n2
    elif c == '+':
        return n1+n2
    else:
        return n1-n2


n = int(input())
l = []
time = (n-1) // 4
remainder = (n-1) % 4
remainnum = 0

for i in range(time):
    l.append((n - i*4) * (n - i*4 - 1) / (n - i*4 - 2) + (n - i*4 - 3))

if remainder == 0:
    remainnum = n - 4*time
elif remainder == 1:
    remainnum =  (n - 4*time)*(n - 4*time -1)
elif remainder == 2:
    remainnum = (n - 4*time)*(n - 4*time -1)/(n - time*4 - 2)
elif remainder == 3:
    remainnum = (n - 4*time) * (n - 4*time -1) / (n - time*4 - 2) + (n - time*4 - 3)

if len(l) > 0:
    count = l[0]
    for i in range(1, len(l)):
        count -= l[i]
    count -= remainnum
else:
    count = remainnum

print(int(count))