rest = eval(input())
veg = int(input())
pri = int(input())
dis = int(input())
ret = []
ans = []
for i in rest:
    if i[2] == veg and i[3] <= pri and i[4] <= dis and veg == 1:
        ret.append(i)
    elif i[3] <= pri and i[4] <= dis and veg == 0:
        ret.append(i)
ret.sort(key=lambda x:(x[1], x[0]),reverse=True)
for j in ret:
    ans.append(j[0])
print(ans)
