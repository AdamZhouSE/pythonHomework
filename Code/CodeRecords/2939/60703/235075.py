K,M=map(int,input().split())

#Str=input();
#nums=Str.split(" ");
#K=int(nums[0]);

#M=int(nums[1]);
list=[1];
temp=1;
tempMin=0;


for i in range(0,K):
    list.sort();
    list.append((int(list[i]))*2+1);
    list.append((int(list[i]))*4+5);

# temp=1;
# for i in range(0,K):
#     temp=4*temp+5;
#     list.append(temp);

list.sort();

#去掉重复
list2=[];
for ele in list:
    if(ele not in list2):
        list2.append(ele);
shortStr="";
for i in range(0,K):
    shortStr=shortStr+str(list2[i]);
print(shortStr);

#
maxIndex=0;
offset=len(shortStr)-M;
beg=0;
result="";
for i in range(0,offset):
    for j in range(beg,M+1):
        if((int(shortStr[j]))>int(shortStr[maxIndex])):
            maxIndex=j;
    result=result+shortStr[maxIndex];
    M+=1;
    beg=maxIndex+1;
    maxIndex+=1;
print(result,end="");