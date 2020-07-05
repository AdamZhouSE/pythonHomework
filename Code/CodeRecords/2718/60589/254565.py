s=list(input())
pairs=eval(input())
movs=[]


while len(pairs)>0: #暴力将对换合成为各个轮换 即暴力实现并查集
    mov=set()
    pair=pairs.pop(0)
    mov.add(pair[0])
    mov.add(pair[1])
    ps=pairs[:]
    has=True
    while has:
        has=False
        ps=pairs[:]
        for p in ps:
            if p[0] in mov or p[1] in mov:
                has=True
                mov.add(p[0])
                mov.add(p[1])
                pairs.remove(p)
    mov=list(mov)
    mov.sort()
    movs.append(mov)


for m in movs:
    arr=[]
    for i in m:
        arr.append(s[i])
    arr.sort()
    for i in m:
        s[i]=arr[0]
        arr.pop(0)
print(''.join(s))