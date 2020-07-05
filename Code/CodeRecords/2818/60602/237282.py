def makeIntList(list):
    count=0;
    while(count<len(list)):
        list[count]=int(list[count]);
        count+=1;
    return list;
def deWu(start,list):
    ans=0;
    list=makeIntList(list);
    start=float(start);
    while(len(list)!=0):
        temp=int(min(list));
        ans+=temp*start;
        if(start>1):
            start-=1;
        else:
            if(start<1):
                start=1;
        list.remove(min(list));
    print(int(ans));

Total=str(input());
Total=Total.split(" ");
studyChapter=str(input());
studyChapter=studyChapter.split(" ");
deWu(Total[1],studyChapter);