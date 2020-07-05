n = int(input());
lengthList = [int(x) for x in input().split()];
length  = len(lengthList);

lengthList.sort();
list1  = lengthList[0:int(length/2)];
list2 = lengthList[int(length/2):];
num1=0;
num2=0;
for i in list1:
    num1+=i;
for i in list2:
    num2+=i;
print(num1*num1+num2*num2);