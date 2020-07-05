house=[int(n) for n in input().split(',')]
loca=[int(n) for n in input().split(',')]
dis=0
if len(loca)==1:
    print(max(abs(loca[0]-house[0]),abs(loca[0]-house[len(house)-1])))
else:
    for i in range(0,len(loca)-1):
        if loca[i+1]-loca[i]>dis:
            dis=loca[i+1]-loca[i]
    if dis%2==0:
        dis=dis//2
    else:
        dis=(dis-1)//2
    if abs(house[0]-loca[0])>dis :
        dis=abs(house[0]-loca[0])
    elif house[len(house)-1]-loca[len(loca)-1]>dis:
        dis=house[len(house)-1]-loca[len(loca)-1]
    print(dis)
