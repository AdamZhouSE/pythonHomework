def func(l:list, k:list) -> list:
    li_small = []
    li_big = []
    li = []
    if len(l) < len(k) :
        li_small = l
        li_big = k
    else:
        li_small = k
        li_big = l
    for i in li_small:
        for j in li_big:
            if (i == j):
                li.append(i)
                li_big.remove(j)
                break
    return li


n = "l = " + input()
m = "k = " + input()
exec(n)
exec(m)


li = func(l,k)
li.sort()
print("[",end="")
for i in li:
    if i == li[0]:
        print(i,end="")
    else:
        print(", ",end="")
        print(i,end="")
print("]")
