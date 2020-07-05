def BrokenCalcu(now,num):
    count=1;
    while(True):
        if(now*2==num or now-1==num):
            if(count==4):
                print(3);
                return;
            if(count==3):
                print(2);
                return
            print(count);
            break;
        else:
            if(now>num):
                now=now-1;
                count+=1;
            else:
                now=now*2;
                count+=1;


now=int(input());
num=int(input());
BrokenCalcu(now,num);