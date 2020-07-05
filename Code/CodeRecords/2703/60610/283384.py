string=input();
sum=string.count("0")+string.count("1");
i=0;
while(pow(i,2)!=sum):
    i+=1;
mid=[]
result=[];
for j in string:
    if(j.isdigit()):
        mid.append(j)
    if(len(mid)==i):
        result.append(mid);
        mid=[];
mid=result;
result=[];
for i in range(len(mid)):
    for j in range(len(mid[i])):
        if(mid[i][j]=="1"):
            result.append([i,j]);
mid=result;
result=[mid[0][0],mid[0][1]];
mid.remove(mid[0])
cout=0;
count=1;
while(mid!=[]):
    j=0;
    while(j!=len(mid)):
        if(mid[j][0] in result) | (mid[j][1] in result):
            result.append(mid[j][0])
            result.append(mid[j][1])
            cout=1
            mid.remove(mid[j]);
        else:
            j+=1;
    if(cout==0):
        count+=1;
        result=[mid[0][0],mid[0][1]]
        mid.remove(mid[0])
    cout=0;
print(count)
