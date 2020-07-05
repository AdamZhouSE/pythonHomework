Neq=int(input())
for i in range(0,Neq):
    l=int(input())
    temp = input().split(" ")
    d = int(input())
    listbig = []
    team = int((l + d - 1) / d)  # 分成的组数
    for x in range(0, team):
        listsmall = []
        for y in range(0, d):
            if (len(temp) >= 1):
                listsmall.append(temp[0])
                temp.pop(0)
        listbig.append(listsmall)
    listbig.append(listbig[0])
    listbig.pop(0)
    listresult=[]
    for m in listbig:
        for n in m:
            listresult.append(n)
    for a in range(0, len(listresult)):
        print(listresult[a], end=" ")
    print("")