list1=list(input().split(","))
str1=list1[0]+"/"
str2=""
for i in range(1,len(list1)-1):
    str2=str2+list1[i]+"/"
str2=str2+list1[len(list1)-1]
print(str1+"("+str2+")")