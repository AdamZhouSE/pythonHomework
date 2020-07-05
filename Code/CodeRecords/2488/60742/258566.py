a = eval(input())
a.sort()
res = []
get_min = True
while a:
    if get_min:
        res.append(a.pop(0))
        get_min = False
    else:
        res.append(a.pop())
        get_min = True
print(res)