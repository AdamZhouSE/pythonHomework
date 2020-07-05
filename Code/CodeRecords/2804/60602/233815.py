def function(string):
    list=string.split("+");
    List=[];
    for integer in list:
        List.append(int(integer));
    list=quickSort(List);
    x=0;
    while x<len(list)-1:
        print(list[x],end="+");
        x+=1;
    print(list[len(list)-1]);

def quickSort(list):
    if(len(list)>1):
        count=1;
        x=list[0];
        leftList=[];
        rightList=[];
        while(count<len(list)):
            if(list[count]>=x):
                rightList.append(list[count]);
            else:
                leftList.append(list[count]);
            count+=1;
        leftList.append(x);
        return quickSort(leftList)+quickSort(rightList);
    else:
        return list;

string=str(input());
function(string);