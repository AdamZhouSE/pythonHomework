import itertools
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
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
n=int(input());
k=int(input());
temp=[];
list=[];
ans=[];
t=n;
while(n>=1):
    temp.append(n);
    n-=1;
for i in itertools.permutations(temp, t):
    tp_list = []
    for j in i:
        tp_list.append(j);
    list.append(tp_list);

for element in list:
    temp="";
    for integer in element:
        temp+=str(integer);
    ans.append(temp);

ans=quickSort(makeIntList(ans));
print(ans[k-1]);