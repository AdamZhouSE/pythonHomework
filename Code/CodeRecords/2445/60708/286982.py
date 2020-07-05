temp=input()
k=0
for i,item in enumerate(temp):
    if item=='\"':
        k=i+1
        temp=temp[k:]
        break
for i,item in enumerate(temp):
    if item=='\"':
        k=i
        str1=temp[0:i]
        temp=temp[i+1:len(temp)]
        break
for i,item in enumerate(temp):
    if item=='\"':
        k=i+1
        temp=temp[k:]
        break
for i,item in enumerate(temp):
    if  item=='\"':
        k = i
        str2 = temp[0:i]
        temp = temp[i + 1:len(temp)]
        break
str1=sorted(str1)
str2=sorted(str2)
result='false'
if(str1==str2):
    result='true'
print(result)
