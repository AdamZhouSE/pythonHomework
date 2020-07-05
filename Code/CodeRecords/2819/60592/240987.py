total = int(input())
gro = list(map(int,input().split(' ')))
gro.sort()
res = 0
countw = [0]*4
for i  in range(0,4):
    countw[i] = gro.count(i+1)
res+=countw[3]
if countw[2]>=countw[0]:
    res+=countw[2]
    if countw[1]%2==0:
        res+=int(countw[1]/2)
    else:
        res+=int(countw[1]/2)+1
else:
    res+=countw[2]
    countw[0]-=countw[2]
    if countw[1]%2==0:
        res+=int(countw[1]/2)
        if countw[0]%4==0:
            res+=int(countw[0]/4)
        else:
            res+=int(countw[0]/4)+1
    else:
        res+=int(countw[1]/2)+1
        if countw[0]%4<=2:
            res+=int(countw[0]/4)
        elif countw[0]%4>2:
            res+=int(countw[0]/4)+1
print(res)