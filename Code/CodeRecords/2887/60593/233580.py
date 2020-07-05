n=int(input())
addup=[0 for i in range(5)]
for i in range(n):
    t,x,y=map(int,input().split())
    addup[t]+=x
    addup[t+2]+=y
if(addup[1]>=addup[3]):
    print('LIVE')
else:
    print('DEAD')
if(addup[2]>=addup[4]):
    print('LIVE')
else:
    print('DEAD')