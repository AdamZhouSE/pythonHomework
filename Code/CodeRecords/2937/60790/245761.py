str1="CODEFESTIVAL2016"
str2=input()
count=0
leng=len(str1)
for i in range(0,leng):
    if(str1[i]!=str2[i]):
        count=count+1
print(count)