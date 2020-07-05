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
        3print(x <= res)
        if x <= res or len(res) <= len(x):
            res = x
print(res)