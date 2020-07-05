t=int(input())
sum1=0;sum2=0
suc1=0;suc2=0
for i in range(t):
    l = eval('[' + input().replace(' ', ',') + ']')
    if l[0]==1:
        sum1+=10
        suc1+=l[1]
    if l[0]==2:
        sum2+=10
        suc2+=l[1]
if suc1>=(sum1//2):
    print('LIVE')
else:
    print('DEAD')
if suc2>=(sum2//2):
    print('LIVE')
else:
    print('DEAD')