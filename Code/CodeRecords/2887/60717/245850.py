n=int(input())
fLive=0
fDead=0
sLive=0
sDead=0
for i in range(0,n):
    list2=input().split()
    for j in range(0,3):
        list2[j]=int(list2[j])
    if list2[0]==1:
        fLive+=list2[1]
        fDead+=list2[2]
    else:
        sLive+=list2[1]
        sDead+=list2[2]
if fLive>=fDead:
    print('LIVE')
else:
    print('DEAD')
if sLive>=sDead:
    print('LIVE')
else:
    print('DEAD')
    