s = input()
group = eval(input())
res = [""]
for x in group:
    jud = True
    for y in x:
        if y not in s:
            jud = False
            break
    if jud:
        #print(x <= res,x)
        if len(x) >= len(res[len(res) - 1]):
            res.append(x)
res.sort()
print(res[len(res) - 1])