str1=input()
str2=input()
count=0
for i in range(0,len(str1)-len(str2)+1):
    str3=str1[i:i+len(str2)]
    if(str2==str3):
        count+=1
print(count,end='')