def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def kthElement(list,k):
    print(list[k-1]) ;

Total=int(input());
i=0;
list=[];
while(i<Total):
    temp=makeIntList(input().split(","));
    j=0;
    while(j<len(temp)):
        list.append(temp[j]);
        j+=1;
    i+=1;
k=int(input());
kthElement(sorted(list),k);