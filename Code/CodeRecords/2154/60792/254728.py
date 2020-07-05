str1=input()
str2=str1[::-1]
len=len(str1)
flag=True
for i in range(0,len):
    if(str1[i]!=str2[i]):
        flag=False
        break
print(flag)