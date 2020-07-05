def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def Lima(list):
    list=makeIntList(list);
    Max=max(list);
    count=0;
    ratio=2;
    while(True):
        for element in list:
            if(Max*ratio%element==0 and((Max*ratio//element)%3==0 or (Max*ratio//element)%2==0 or Max==element)):
                count+=1;
        if(count==len(list)):
            print("Yes");
            break;
        else:
            if(ratio==2):
                count=0;
                ratio+=1;
            else:
                print("No");
                break;

Total=int(input());
list=str(input());
list=list.split(" ");
Lima(list);