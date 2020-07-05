from collections import Counter
result=[];
j=0;
for i in range(10):
    tempres=[];
    while(len(str(2**j))==i):
        tempres.append(str(2**j))
        j+=1;
    result.append(tempres);
result=result[1:]
# print(result)
nums=input();
numc=Counter(nums);
# c1=Counter("abc")
# c2=Counter("abc")
numslinker=result[len(nums)-1];
finout=False;
for i in numslinker:
    tempc=Counter(i);
    if tempc==numc:
        finout=True;
if(finout):
    print("True")
else:print("False")