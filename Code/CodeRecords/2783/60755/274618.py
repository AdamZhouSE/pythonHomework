num = int(input())
game=[]
for i in range(num):
    game.append(input().split(" "))
res={}
max=-1
name=""
for i in game:
    if i[0] in res:
        res[i[0]] = res[i[0]]+int(i[1])
    else:
        res[i[0]] = int(i[1])
    if res[i[0]]>max:
        max = res[i[0]]
        name = i[0]
print(name)
