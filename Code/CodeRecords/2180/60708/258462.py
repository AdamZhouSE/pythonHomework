def cut(str,l):
    list=[]
    for i in range(0,len(str)-l+1):
        list.append(str[i:i+l])
    return list
str1=input()
str2=input()
l=0
if(len(str1)<len(str2)):
    l=len(str1)
else:
    l=len(str2)
result=0
for i in range(1,l):
    list1=cut(str1,i)
    list2=cut(str2,i)
    for x in list1:
        for y in list2:
            if x==y:
                result=result+1
print(result,end="")