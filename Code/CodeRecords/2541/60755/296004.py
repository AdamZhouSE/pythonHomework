n = int(input())
all = input()[2:-2].split("],[")
a = []
for i in all:
    a.append(i.split(","))
res = []
pre = []
p = []
for i in a:
    if pre.count(i[0]) == 0:
        pre.append(i[0])
while len(a) != 0:
    flag = False
    for i in a:
        if pre.count(i[1]) == 0 and res.count(int(i[1])) == 0:
            res.append(int(i[1]))
            res.append(int(i[0]))
            a.remove(i)
            pre.remove(i[0])
            flag = True
            break
        if flag:
            break
    for i in a:
        if pre.count(i[1]) == 0:
            if res.count(int(i[0]))==0:
                res.append(int(i[0]))
            a.remove(i)
            if pre.count(i[0])!=0:
                pre.remove(i[0])
            break
print(res)
