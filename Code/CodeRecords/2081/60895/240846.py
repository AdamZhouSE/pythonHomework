str1=input()
str2=input()
len1=len(str1)
len2=len(str2)
result=0
for i in range(0,len1-len2+1):
    temp=str1[i:i+len2]
    if temp==str2:
        result=result+1
print(result,end='')