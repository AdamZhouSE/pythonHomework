string=input();
result="";
resultList=[];
for i in range(len(string)):
    result=string[i:]+string[0:i];
    resultList.append(result);
result="";
resultList.sort(key=None,reverse=False);
for i in resultList:
    result=result+i[-1];
print(result,end="");