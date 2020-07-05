def computeSubString(inp):
    aIndex,bIndex,cIndex=[],[],[]
    for i in range(len(inp)):
        if inp[i]=='a':
            aIndex.append(i)
        elif inp[i]=='b':
            bIndex.append(i)
        elif inp[i]=='c':
            cIndex.append(i)
    res=0
    biggerX=0
    for x in aIndex:
        biggerX+=1
        biggerY=0
        for y in bIndex:
            if y>x:
                biggerY+=1
                biggerZ=0
                for z in cIndex:
                    if z>y:
                        biggerZ+=1
                        res+=biggerY*biggerX*biggerZ
    return res

cases=int(input())
for _ in range(cases):
    inp=input()
    res=computeSubString(inp)
    print(res)