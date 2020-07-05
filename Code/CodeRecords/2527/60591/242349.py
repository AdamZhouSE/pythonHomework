temp = input()[2:-2].split("],[")
tem = {}
for t in temp:
    rest = list(map(int,t.split(",")))
    tem[rest[0]] = (rest[1],rest[2],rest[3],rest[4])
veg = eval(input())
maxPrice = eval(input())
maxDistance = eval(input())

test = tem.copy()
key = list(tem.keys())
for m in key:
    if(tem[m][2] > maxPrice or tem[m][3] > maxDistance):
        del tem[m]
    if(veg == 1):
        if(tem[m][1]!=veg):
            del tem[m]

key = list(tem.keys())

res = []
for k in key:
    res.append([tem[k][0],k])
res.sort(reverse=True)
result = []
for re in res:
    result.append(re[1])
print(result)

