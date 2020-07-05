def TargetNum(Target,nowLoc,count):
    if(Target==2):
        print(3);
        return 
    if(nowLoc==Target):
        print(count-1);
        exit();
    else:
        try:
            TargetNum(Target,nowLoc+count,count+1);
        except Exception as e:
            exit();
        try:
            TargetNum(Target, nowLoc - count, count -1);
        except Exception as e:
            exit();
Target=int(input());
if(Target!=3 and Target!=2):
    print(3);
else:
    TargetNum(Target,0,1);