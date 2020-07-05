def func(l:list) -> list:
    i = 0
    while (i < len(l) -1):
        if int(l[i][1]) >= int(l[i + 1][0]):
            l[i][1] = l[i + 1][1]
            del l[i + 1]
        else:
            i+=1
    return l

n = "l = " + input()
exec(n)
li = func(l)
print("[",end="")
for i in li:
    if i != li[len(li)-1]:
        print(i, end=", ")
    else:
        print(i,end="")
print("]")