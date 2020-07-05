s = input()
group = eval(input())
res = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
for x in group:
    jud = True
    for y in x:
        if y not in tem:
            jud = False
            break
    if jud:
        print(x <= res)
        if x <= res:
            if len(res) <= len(x):
                res = x
print(res)