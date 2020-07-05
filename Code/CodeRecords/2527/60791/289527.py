rest = eval(input())
venga = int(input())
price = int(input())
dist = int(input())
res = []
for i in range(len(rest)):
    if venga == 1:
        if rest[i][2] == 1 and rest[i][3] <= price and rest[i][4] <= dist :
            res.append(rest[i])
    else:
        if rest[i][3] <= price and rest[i][4] <= dist :
            res.append(rest[i])
res = sorted(res,key = (lambda x: (-x[1],-x[0])))
temp = []
for item in res:
    temp.append(item[0])
print(temp)