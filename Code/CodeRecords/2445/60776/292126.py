a=input().split(' ')
str1=a[2].replace("\"","",1)
str1=str1.replace("\",","")
str2=a[5].replace("\"","",2)
new_str1=[]
for i in range(0,len(str1)):
    new_str1.append(str1[i])
new_str2=[]
for i in range(0,len(str2)):
    new_str2.append(str2[i])
new_str1.sort()
new_str2.sort()
if new_str1==new_str2:
    print("true")
else:
    print("false")