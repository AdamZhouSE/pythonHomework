def getSubstrList(string,n):
    substrList=[]
    for i in range(n):
        for j in range(i,n):
            substrList.append(string[i:j+1])
    return substrList

string1=input()
string2=input()
n1=len(string1)
n2=len(string2)
string1List=getSubstrList(string1,n1)
string2List=getSubstrList(string2,n2)
sum=0
for i in range(len(string1List)):
    sum+=string2List.count(string1List[i])
print(sum,end='')
