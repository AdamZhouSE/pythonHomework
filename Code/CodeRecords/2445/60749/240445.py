str1=list(input())
str2=list(input())
for x in str1:
    if x in str2:
        str2.remove(x)
if len(str2)==0:
    print(True)
else:
    print(False)