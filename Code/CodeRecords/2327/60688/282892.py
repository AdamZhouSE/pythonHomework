strlist=list(input())
numslsit=[i for i in range(len(strlist)+1)]
result=[];
for i in range(len(strlist)):
    if(strlist[i]=="D"):
        result.append(max(numslsit));
        numslsit.remove(max(numslsit));
    else:
        result.append(min(numslsit));
        numslsit.remove(min(numslsit));
result.extend(numslsit)
print(result)