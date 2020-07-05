def one(bulb):
    re=[(not i) for i in bulb]
    return re
def two(bulb):
    re=[]
    for i in range(0,len(bulb)):
        if i%2==1:
            re.append(not bulb[i])
        else:
            re.append(bulb[i])
    return re
def three(bulb):
    re=[]
    for i in range(0,len(bulb)):
        if i%2==0:
            re.append(not bulb[i])
        else:
            re.append(bulb[i])
    return re
def four(bulb):
    re = []
    for i in range(0, len(bulb)):
        if i%3==0:
            re.append(not bulb[i])
        else:
            re.append(bulb[i])
    return re

n=int(input())
m=int(input())
bulb=[True for i in range(0,n)]
re=[one(bulb),two(bulb),three(bulb),four(bulb)]
if m==1:
    r=[]
    for i in re:
        if not i in r:
            r.append(i)
    print(len(r))
else:
    for i in range(0,4):
        re.append(four(re[i]))
    r=[]
    for i in re:
        if not i in r:
            r.append(i)
    print(len(r))