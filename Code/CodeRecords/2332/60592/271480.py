base = int(input())
tar = int(input())
res = 0
fun = []
te = 0
tem = tar
while tem != 0:
    i = 0
    if tem == 1:
        te += 1
        break
    mark = 0
    while mark <= tem:
        mark = pow(base,i)
        i+=1
    te+=i-3
    mark/=base
    tem-=mark
    if tem!= 0:
        te+=1
fun.append(te)
te = 0
tem = tar
while tem != 0:
    i = 0
    if tem == 1 or tem == -1:
        te+=1
        break
    mark = 0
    while mark < abs(tem):
        mark = pow(base,i)
        i+=1
    te+=i-2
    if tem < 0:
        tem+=mark
    elif tem>0:
        tem-=mark
    if tem != 0:
        te+=1
fun.append(te)
print(min(fun))