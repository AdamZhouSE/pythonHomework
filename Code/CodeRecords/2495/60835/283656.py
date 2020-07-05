s = input()
group = eval(input())
res = "z"
for x in group:
    jud = True
    for y in x:
        if y not in s:
            jud = False
            break
    if jud:
        #print(x <= res,x)
        if len(res) <= len(x):
            if x <= res:
                res = x
print(res)