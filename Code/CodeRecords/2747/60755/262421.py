def onedif(a,b):
    A = list(a)
    B = list(b)
    num = 0
    for i in A:
        num = num + B.count(i)
    return num == len(B)-1



def solve(fro , to ,all,already,res):
    temp = []
    for i in all:
        tall = all.copy()
        talready = already.copy()
        if onedif(fro,i):
            talready.append(i)
            tall.remove(i)
            if onedif(i,to):
                talready.append(to)
                res.append(talready)
            else:
                solve(i,to,tall,talready,res)

    return res


fro = input()
to = input()
origin = input().replace("\",\"", " ")
all = origin[2:-2].split(" ")
res = solve(fro, to, all[:-1], [fro], [])
min = 10000
for i in res:
    if len(i)<min:
        min = len(i)
result = []
for i in res:
    if len(i) == min:
        result.append(i)
if all.count(to)==0:
    result = []
print(result)


