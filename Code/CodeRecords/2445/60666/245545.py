str1,str2=input().split(",")
lst1=list(str1)
lst2=list(str2)
flag="true"
for element in lst1:
    if not element:
        flag="false"
print(flag)