s = input()
group = eval(input())
res = []
for x in group:
    jud = True
    for y in x:
        if y not in s:
            jud = False
            break
    if jud:
        #print(x <= res,x)
        res.append(x)
res.sort()
#print(res)
ind = res[0][0]
for x in range(len(res)):
    if ind != res[x][0]:
        if x != 0:
            print(res[x - 1])
            break
        else:
            print(res[x])
            break