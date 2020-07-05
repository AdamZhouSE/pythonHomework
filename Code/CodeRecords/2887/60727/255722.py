pings = int(input())
suc1,suc2,def1,def2=0,0,0,0
for i in range(0,pings):
    data = input().split(' ')
    data = list(map(int,data))
    if data[0]==1:
        suc1+=data[1]
        def1+=data[2]
    if data[0]==2:
        suc2+=data[1]
        def2+=data[2]
if suc1>=def1:
    print('LIVE')
else:
    print('DEAD')
if suc2>=def2:
    print('LIVE')
else:
    print('DEAD')