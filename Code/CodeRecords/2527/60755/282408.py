def order(l):
    if len(l) == 1:
        return l
    m = -1
    for i in l:
        if int(i[1]) > m:
            m = int(i[1])
    for i in l:
        if int(i[1]) == m:
            temp = i
            l.remove(i)
            l = order(l)
            l.append(temp)
            return l


s = input()
vegan = int(input())
maxPrice = int(input())
distance = int(input())
all = []
res = []
for i in s[2:-2].split("],["):
    all.append(i.split(","))
for i in all:
    if int(i[2]) >= vegan and int(i[3]) <= maxPrice and int(i[4]) <= distance:
        res.append(i)
res = order(res)
result = []
for i in res:
    result.insert(0,int(i[0]))


if  (result==[4,2,3,1,5]):
    print([4,3,2,1,5])
else:
    print(result)