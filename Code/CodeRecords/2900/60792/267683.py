str1=input()
count=0
for i in range(0,len(str1)):
    if str1[i]!=" ":
        count=count+1
print(count,end="")        