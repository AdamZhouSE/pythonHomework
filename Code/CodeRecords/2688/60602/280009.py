import itertools
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def Ssum(list):
    i=0;
    count=0;
    while(i<len(list)):
        count+=list[i];
        i+=1;
    return count;
def perfectSum(list,SUM):
    i=1;
    count=0;
    while(i<len(list)):

        for element in itertools.combinations(list,i):
            if(Ssum(element)==SUM):
                count+=1;

        i+=1;
    print(count);

Total=int(input());
i=0;
while(i<Total):
    n=int(input());
    list=makeIntList(input().split(" "));
    sum=int(input());
    perfectSum(list,sum);
    i+=1;