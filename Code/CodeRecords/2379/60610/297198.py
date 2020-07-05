string=input();
#0,1,2,3,上右下左
tar=0;
mid=[0,0];
count=0;
for j in range(4):
    for i in string:
        if(i=="G"):
            if(tar==0):
                mid[1]+=1;
            elif(tar==2):
                mid[1]-=1;
            elif(tar==1):
                mid[0]+=1;
            else:
                mid[0]-=1;
        elif(i=="L"):
            if(tar==0):
                tar=3;
            else:
                tar-=1;
        elif(i=="R"):
            if (tar == 3):
                tar = 0;
            else:
                tar += 1;
    if(mid==[0,0]):
        count=1;
if(count==0):
    print("False");
else:
    print("True")