a = input()
aa = a[1: len(a)-1].split(",")
b = []
ans = []
for x in aa:
    b.append(int(x))
d = len(b)//3
b.sort()
while len(b) != 0:
    x = d
    temp = b[0]
    b.pop(0)
    if len(b) == 0:
        break
    while b[0] == temp:
        b.pop(0)
        x = x - 1
        if x == 0:
            ans.append(temp)
        if len(b) == 0:
            break
print(ans)