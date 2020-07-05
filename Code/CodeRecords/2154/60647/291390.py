n=int(input())
str1=str(n)
strr=''
for i in range(len(str1)):
    strr+=str1[len(str1)-1-i]
if strr==str1:
    print('True')
else:
    print('False')