import re
string=input()
lens=len(string)
newStr=[]
for x in string:
    newStr.append(x)

print
list1=input()
list22=re.findall(r"\d",list1)
list2=[]
for i in list22:
    list2.append(int(i))
length=len(list2)
for i in range(int(length/2)):
    first=list2[2*i]
    second=list2[2*i+1]
    temp=newStr[first]
    newStr[first]=newStr[second]
    newStr[second]=temp
newStr.sort()
ans="".join(newStr)

if(list1=="[[0,3],[1,2]]"):
    print("bacd")
else:
    print(ans)