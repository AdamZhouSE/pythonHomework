def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def calcuRain(list):
    if(len(list)<=2):
        return 0;
    temp=[];
    for element in list:
        temp.append(element);
    i=1;
    count=0;
    temp.remove(max(temp));
    MAX=max(list);
    SECMAX=max(temp);
    sum=min(MAX,SECMAX);
    if((list.index(SECMAX)==0 and list.index(MAX)==len(list)-1) or (list.index(SECMAX)==len(list)-1 and list.index(MAX)==0)):
        while(i<len(list)-1):
            count+=sum-list[i];
            i+=1;
        return count;
    else:
        if(list.index(SECMAX)<list.index(MAX)):
            i=list.index(SECMAX)+1;
            while (i < list.index(MAX)):
                count += sum - list[i];
                i += 1;
            return calcuRain(list[0:list.index(SECMAX)+1])+count+calcuRain(list[list.index(MAX):]);
        elif(list.index(SECMAX)==list.index(MAX)):
            return 0;
        else:
            i=list.index(MAX)+1;
            while (i < list.index(SECMAX) - 1):
                count += sum - list[i];
                i += 1;
            return calcuRain(list[0:list.index(MAX)+1])+count+calcuRain(list[list.index(SECMAX):]);

Total=int(input());
while(Total>0):
    temp=int(input());
    list=str(input());
    list=list.split(" ");
    print(calcuRain(makeIntList(list)));
    Total-=1;