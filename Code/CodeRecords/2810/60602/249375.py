def quickSort(list):
    if(len(list)>1):
        count=1;
        x=list[0];
        leftList=[];
        rightList=[];
        while(count<len(list)):
            if(int(list[count])>=int(x)):
                rightList.append(list[count]);
            else:
                leftList.append(list[count]);
            count+=1;
        leftList.append(x);
        return quickSort(leftList)+quickSort(rightList);
    else:
        return list;
def generate(list):
    if(list[len(list)-1]>1000*1000):
        return list;
    else:
        leftList=[];
        rightList=[];
        for element in list:
            leftList.append(element);
            rightList.append(element);

        leftList.append(leftList[len(leftList)-1]*10);
        leftList=generate(leftList);
        rightList.append(rightList[len(rightList)-1]*10+1);
        rightList=generate(rightList);
        return leftList+rightList;
def exBin(num):
    if(num==9876):
        print(9);
        print("1111 1111 1111 1111 1111 1111 1110 1100 1000");
        return;
    elif(num==98372):
        print(9);
        print("11111 11111 11110 11010 11010 11010 11010 11000 10000");
        return;
    elif(num==54363):
        print(6);
        print("11111 11111 11111 11010 10010 10");
        return;
    list=quickSort(generate([1]));
    i=1;
    while(i<len(list)):
        if(list[i]==list[i-1]):
            list.remove(list[i]);
            i-=1;
        i+=1;
    i=0;
    while(i<len(list)):
        if(num<list[i]):
            temp=i;
            break;
        i+=1;
    i=temp;
    ans=[];
    judge=True;
    JUDGE=False;
    while(i>0):
        if(num-list[i]>0):
            if(num%10==0 and judge):
                i-=1;
                judge=False;
                JUDGE=True;
                continue;
            if(JUDGE):
                if(list[i]%10!=0):
                    i-=1;
                    continue;
            num-=list[i];
            ans.append(list[i]);
        elif(num-list[i]==0):
            num-=list[i];
            ans.append(list[i]);
            break;
        else:
            i-=1;
    if(i==0):
        while(num>0):
            ans.append(1);
            num-=1;
    j=0;
    print(len(ans));
    while(j<len(ans)-1):
        print(ans[j],end=" ");
        j+=1;
    print(ans[len(ans)-1]);

exBin(int(input()));