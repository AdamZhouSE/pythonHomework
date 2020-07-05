def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;

def localSort(list,judge,l,r):
    if(judge==0):
        return list[0:l-1]+sorted(list[l-1:r])+list[r:];
    else:
        temp =sorted(list[l - 1:r]);
        temp.reverse();
        return list[0:l - 1] + temp + list[r:];

size=input().split(" ");
m=int(size[0]);
n=int(size[1]);
list=makeIntList(input().split(" "));
i=0;
while(i<n):
    tempList=makeIntList(input().split(" "));
    judge=tempList[0];
    l=tempList[1];
    r=tempList[2];
    list=localSort(list,judge,l,r);
    i+=1;
q=int(input());
print(list[q-1]);