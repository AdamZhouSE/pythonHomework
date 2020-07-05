target=int(input())
position=input();
position=position.replace("[","");
position=position.replace("]","");
position=list(map(int,position.split(",")));
speed=input();
speed=speed.replace("[","");
speed=speed.replace("]","");
speed=list(map(int,speed.split(",")));

os=sorted(position);
count=1;
for i in range(len(os)-1):
    if(speed[position.index(os[i])]<speed[position.index(os[i+1])]):
        count+=1;
    else:
        dis=os[i+1]-os[i];
        spe=speed[position.index(os[i])]-speed[position.index(os[i+1])];
        if(dis/spe*speed[position.index(os[i+1])]>target):
            count+=1;
print(count)