str1="CODEFESTIVAL2016"
str2=input()
total=0
for i in range(len(str2)):
    if str1[i]!=str2[i]:
        total+=1
print(total)
