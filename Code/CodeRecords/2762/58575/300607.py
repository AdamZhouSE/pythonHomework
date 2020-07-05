import math

num=int(input())
pos=["N","W","S","E"]
res=list()
for i in range(num):
    posCurr=pos[0]
    x=0
    y=0

    number=int(input())
    str1=input().split(" ")
    j=0
    while j<2*number:
        posChange=str1[j]
        j=j+1
        displace=str1[j]
        j=j+1
        if posChange=='U':
            if posCurr=='N' or posCurr=='S':
                x=x-(pos.index(posCurr)-1)*int(displace)
            elif posCurr=='E' or posCurr=='W':
                y=y+(pos.index(posCurr)-2)*int(displace)
        elif posChange=='D':
            posCurr=pos[pos.index(posCurr)+2]
            if posCurr=='N' or posCurr=='S':
                x=x-(pos.index(posCurr)-1)*int(displace)
            elif posCurr=='E' or posCurr=='W':
                y=y-(pos.index(posCurr)-2)*int(displace)
        elif posChange=='L':
            posCurr = pos[pos.index(posCurr) + 1]
            if posCurr == 'N' or posCurr == 'S':
                x = x - (pos.index(posCurr) - 1) * int(displace)
            elif posCurr == 'E' or posCurr == 'W':
                y = y - (pos.index(posCurr) - 2) * int(displace)
        else:
            posCurr = pos[pos.index(posCurr) - 1]
            if posCurr == 'N' or posCurr == 'S':
                x = x - (pos.index(posCurr) - 1) * int(displace)
            elif posCurr == 'E' or posCurr == 'W':
                y = y - (pos.index(posCurr) - 2) * int(displace)
    length=int(math.sqrt(x**2+y**2))
    res.append(str(length)+" "+posCurr)
for i in res:
    print(i)