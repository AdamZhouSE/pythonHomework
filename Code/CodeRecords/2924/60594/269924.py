row=[int(n) for n in input().split()]
n=row[0]
r=row[1]
avg=row[2]
lunwenshu=0
kaoshi=[]
for i in range(n):
    row1=[int(n) for n in input().split()]
    kaoshi.append(row1)
zongfen=0
for i in kaoshi:
    zongfen+=i[0]
cha=avg*n-zongfen
while cha > 0:
    min = 10000000000000000
    biaoji = 0
    for index in range(len(kaoshi)):
        if kaoshi[index][1] < min:
            biaoji = index
            min = kaoshi[index][1]
    if r - kaoshi[biaoji][0] > 0:
        if r - kaoshi[biaoji][0] > avg*n-zongfen:
            xuyao = avg*n-zongfen
        else:
            xuyao = r - kaoshi[biaoji][0]
        zongfen += xuyao
        lunwenshu += xuyao * kaoshi[biaoji][1]
        cha = avg * n - zongfen
    kaoshi.remove(kaoshi[biaoji])
print(lunwenshu)