num=int(input())
l=[]
for i in range(num):
    step=int(input())
    todo=list(input().split(" "))
    directions=todo[::2]
    steps=list(map(int,todo[1::2]))
    towards=["N","E","S","W"]
    resultDirect="N"
    assistDirect=["N"]
    x=0
    y=0
    for j in range(1,len(directions)):
        if directions[j]=="R":
            resultDirect=towards[(towards.index(resultDirect)+1)%len(towards)]
            assistDirect.append(resultDirect)
        elif directions[j]=="L":
            resultDirect=towards[(towards.index(resultDirect)-1+len(towards))%len(towards)]
            assistDirect.append(resultDirect)
        elif directions[j]=="D":
            resultDirect=towards[(towards.index(resultDirect)+2)%len(towards)]
            assistDirect.append(resultDirect)
        else:
            assistDirect.append(resultDirect)
    for j in range(len(steps)):
        if assistDirect[j]=="N":
            y+=steps[j]
        elif assistDirect[j]=="E":
            x+=steps[j]
        elif assistDirect[j]=="S":
            y-=steps[j]
        else:
            x-=steps[j]
    pos=int((abs(x)**2+abs(y)**2)**0.5)
    print(pos,end=" ")
    print(resultDirect)