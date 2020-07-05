str1=input()
str2='CODEFESTIVAL2016'
ans=0
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        ans=ans+1
print(ans)