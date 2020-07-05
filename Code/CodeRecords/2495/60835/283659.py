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
        res.append(res)
res.sort()
print(res[len(res) - 1])