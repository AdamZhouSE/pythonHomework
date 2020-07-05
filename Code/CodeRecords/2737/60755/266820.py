string = input()
l = string[1:-1].split(",")
res = []
for i in l:
    if l.count(i)>int(len(l)/3) and res.count(int(i))==0:
        res.append(int(i))
print(res)