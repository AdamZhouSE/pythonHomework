def combine(l):
    for i in range(len(l)):
        for k in range(i+1,len(l)):
            if int(l[i][1]) >= int(l[k][0]):

                temp = [l[i][0], l[k][1]]
                l.remove(l[k])
                l.remove(l[i])
                l.insert(i, temp)
                combine(l)
                break
    return l

string = input()
l = string[2:-2].split("],[")
res = []
for i in l:
    res.append(i.split(","))
res = combine(res)
s = ""
for i in res:
    s = s + "["+i[0]+", "+i[1]+"]"+", "
s = "["+s[:-2]+"]"

print(s)
