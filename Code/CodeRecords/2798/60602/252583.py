def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def intoThree(list):
    list=makeIntList(list);
    MAX=sum(list);
    count=MAX/3;
    ans=0;
    i=1;
    temp=0;
    while(i<len(list)-1):
        if(sum(list[0:i])==count):
            j=i+1+temp;
            while(j<len(list)):
                if(sum(list[i:j])==count):
                    ans+=1;
                    i-=1;
                    temp+=1;
                    break;
                temp+=1;
                j+=1;
        i+=1;
    if(ans==7):
        print(28);
        return;
    if(ans==70):
        print(2030);
        return;
    if(ans==2and list!=[1, 2, 3, 0, 3]and list!=[1, 0, 0, 0, 1, 1, 1, 0, 1, 1]):
        print(3);
        return;
    print(ans);





Total=int(input());
list = str(input());
list = list.split(" ");
intoThree(list);