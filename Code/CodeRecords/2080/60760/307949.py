def func(vers:list,maps:list,start:str):
    res=[start]
    length=len(vers)
    temp=[start]
    while len(res)<length:
        temp2 = []
        for j in temp:

            locate=vers.index(j)
            for i in range(length):
                if maps[locate][i]!=0 and res.count(vers[i])<1:
                   res.append(vers[i])
                   temp2.append(vers[i])
        temp=list(temp2)
    return res

tests=int(input())
vers=[]
maps=[]
res=[]
for i in range(tests):
    first=input().split(' ')
    numofver=int(first[0])
    starts=(first[1])
    vers=(input().split(' '))
    for j in range(numofver):
        maps.append(list(map(int,input()[2:].split(' '))))
    res.append(func(vers,maps,starts))
for i in res:
    for j in i:
        if i[-1]!=j:
            print(j,end=' ')
        else:
            print(j)
