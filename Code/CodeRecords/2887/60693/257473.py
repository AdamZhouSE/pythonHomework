opes=int(input())
onelive,twolive=0,0
one_op,two_op=0,0
for i in range(opes):
    op=list(map(int,input().split()))
    if op[0]==1:
        onelive+=op[1]
        one_op+=1
    if op[0]==2:
        twolive+=op[1]
        two_op+=1
if onelive>=one_op*5:print('LIVE')
else:print('DEAD')
if twolive>=two_op*5:print('LIVE')
else:print('DEAD')