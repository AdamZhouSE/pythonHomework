def AliceGame(num,now,count):
    if(num%now==0 and num>0):
        AliceGame(num-now,now,count+1);
    else:
        if(count%2==0):
            print(True);
        else:
            print(False);


num=int(input());
if(num==1):
    print(0);
else:
    AliceGame(num,1,0);