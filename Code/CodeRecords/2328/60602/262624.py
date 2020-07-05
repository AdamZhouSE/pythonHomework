def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def MaxTime(list):
    try:
        temp=[];
        i=0;
        ans="";
        while(i<len(list)):
            if(list[i]>=0 and list[i]<=2):
                temp.append(list[i]);
            i+=1;
        if(max(temp)==2):
            ans+=str(max(temp));
            list.remove(max(temp));
            temp=[];
            i=0;
            while (i < len(list)):
                if (list[i] >= 0 and list[i] <= 3):
                    temp.append(list[i]);
                i += 1;
            ans+=str(max(temp));
            list.remove(max(temp));
        else:
            ans+=str(max(temp));
            list.remove(max(temp));
            ans+=str(max(list));
            list.remove(max(list));
        ans+=":";
        temp=[];
        i=0;
        while(i<len(list)):
            if(list[i]>=0 and list[i]<=5):
                temp.append(list[i]);
            i+=1;
        ans+=str(max(temp));
        list.remove(max(temp));
        ans+=str(list[0]);
        print(ans);
    except Exception as e:
        print("");


list=makeIntList(str(input()).split(","));
MaxTime(list);