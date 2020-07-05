num=int(input());
for i in range(num):
    length=input();
    nums=list(map(int,input().split()));
    mid=[[nums.count(nums[i]),nums[i]] for i in range(len(nums))];
    mid=sorted(mid,reverse=True);
    result=[];
    cmid=[];
    count=1;
    while(count!=0):
        cout=0;
        for i in range(len(mid)-1):
            if(mid[i][0]==mid[i+1][0]):
                if(mid[i][1]>mid[i+1][1]):
                    t=mid[i][1]
                    mid[i][1]=mid[i+1][1]
                    mid[i+1][1]=t
                else:
                    cout+=1;
            else:
                cout+=1;
        if(cout==len(mid)-1):
            count=0;
    for i in mid:
        print(str(i[1]),end=" ");
    print()