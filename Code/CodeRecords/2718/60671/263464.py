import re
string=input()
lens=len(string)
newStr=["0"]*lens


list1=input()
list22=re.findall(r"\d",list1)
list2=[]
for i in list22:
    list2.append(int(i))
length=len(list2)
for i in range(int(length/2)):
    first=list2[2*i]
    second=list2[2*i+1]
    newStr[first]=string[second]
    newStr[second]=string[first]
ans="".join(newStr)
print(ans)