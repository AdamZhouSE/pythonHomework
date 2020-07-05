def solve(s1,s2,l):
    if int(s1[1]) >= int(s2[0]):
        temp = [s1[0], s2[1]]
        l.remove(s1)
        l.remove(s2)
        l.append(temp)
        l.sort()

    # elif int(s1[1]) >= int(s2[0])




def combine(l):
    for i in range(len(l)):
        for k in range(i+1,len(l)):
            if int(l[i][1]) >= int(l[k][0]) and int(l[k][1] > int(l[i][1])):

                temp = [l[i][0], l[k][1]]
                l.remove(l[k])
                l.remove(l[i])
                l.insert(i, temp)
                combine(l)
                l.sort()
                break
            elif int(l[i][0]) <= int(l[k][0]) and int(l[i][1]) >= int(l[k][1]) :
                l.remove(l[k])
                combine(l)
                l.sort()
                break
    return l


string1 = input()
string2 = input()
l = (string1[2:-1]+","+string2[:-1]).split("],[")
res = []
for i in l:
    res.append(i.split(","))
for i in range(len(res)):
    res[i] = [int(res[i][0]), int(res[i][1])]
res.sort()
res = combine(res)
s = ""
for i in res:
    s = s + "["+str(i[0])+", "+str(i[1])+"]"+", "
s = "["+s[:-2]+"]"

print(s)

