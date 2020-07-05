str1=input()
str2=input()
biaoji=0
isright="True"
for i in range(0,len(str1)):
    if str1[i] not in str2[biaoji:len(str2)]:
        isright="False"
    else:
        for j in range(biaoji,len(str2)):
            if str2[j]==str1[i]:
                biaoji=j+1
print(isright)