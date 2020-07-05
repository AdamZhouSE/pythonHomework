num=input().split(",");
index_1=[];
tar=0;
for i in range(len(num)):
    if(num[i]=='1'):
        index_1.append(i);
if(len(index_1)%3!=0):
    tar=1;
firstindex=index_1[0];
secondindex=index_1[len(index_1)//3];
thirdindex=index_1[len(index_1)//3*2];
if(secondindex-firstindex<len(num)-thirdindex)|(thirdindex-secondindex<len(num)-thirdindex):
    tar=1;
while(thirdindex<len(index_1)):
    if(index_1[firstindex]!=index_1[thirdindex])|(index_1[secondindex]!=index_1[thirdindex]):
        tar=1;
    firstindex+=1;
    secondindex+=1;
    thirdindex+=1;
if(tar==1):
    print("[-1, -1]");
else:
    print([firstindex,secondindex+1]);