def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def CalcuNum(list,count):
    print(list[0]+(count-1)*(list[1]-list[0]));

Total=int(input());
i=0;
while(i<Total):
    list=makeIntList(input().split(" "));
    count=int(input());
    CalcuNum(list,count);
    i+=1;