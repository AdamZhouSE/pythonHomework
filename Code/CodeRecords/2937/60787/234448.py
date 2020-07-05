str1=list("CODEFESTIVAL2016")
str2=list(input())
num=0
for i in range(0,16):
    if not str1[i]==str2[i]:
        num+=1
print(num)