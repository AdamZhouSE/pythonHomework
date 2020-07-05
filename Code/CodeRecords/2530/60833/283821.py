str1=str(input())
str2=str(input())
out=''
for i in str2:
    if str1.count(i)==0:
        out+=i
for i in str1:
    for j in range(str2.count(i)):
        out+=i
print(out)