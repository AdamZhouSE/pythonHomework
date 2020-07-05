def isSubstring(str3,str1):
    flag=False
    j=0
    for i in range(0,len(str1)):
        if str1[i]==str3[j]:
            if j==len(str3)-1:
                flag=True
                break
            j+=1
    return flag

str1=input()
str2=input()
str2=str2[1:len(str2)-1]
list1=list(str2.split(","))
s=""
for i in range(0,len(list1)):
    str3=list1[i][1:len(list1[i])-1]
    if isSubstring(str3,str1):
        if len(str3)>len(s):
            s=str3
print(s)