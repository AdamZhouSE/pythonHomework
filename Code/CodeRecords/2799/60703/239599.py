n=int(input());
StrList = input().split();
NumList = [int(x) for x in StrList];
length = len(NumList);#除了2和3以外的因子相同
reducedList = [];
for i in NumList:
    temp=i;
    while(temp%2==0):
        temp=int(temp/2);
    while(temp%3==0):
        temp = int(temp/3);
    reducedList.append(temp);
reducedList = list(set(reducedList));
if(len(reducedList)==1):
    print("Yes");
else:
    print("No");