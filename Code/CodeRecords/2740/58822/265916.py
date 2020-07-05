n=input()
list=n[1:len(n)-1].split(',')
for i in range(len(list)):
    if(list[i]=='"00:00"'):
        list.append('"24:00"')
min=24*60
for i in range(0,len(list)):
    cha=0
    for k in range(i+1,len(list)):
        if(int(list[i][1:3])<int(list[k][1:3])):
            shicha=(abs(int(list[i][1:3])-int(list[k][1:3])))*60
            fen=0-int(list[i][4:6])+int(list[k][4:6])
        else:
            if(int(list[i][1:3])>int(list[k][1:3])):
                shicha=(abs(int(list[i][1:3])-int(list[k][1:3])))*60
                fen=int(list[i][4:6])-int(list[k][4:6])
            else:
                fen=abs(int(list[i][4:6])-int(list[k][4:6]))
        cha=shicha+fen
        if(cha<min):
            min=cha
print(min)