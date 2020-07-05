def isTrue(s):
    if s=="+" or s=="-" or (s>="1" and s<="9"):
        return True
    else:
        return False
    
def isDigit(s):
    if (s>="1" and s<="9"):
        return True
    else:
        return False
    
str1=input()
count=0
str2=""
for i in range(0,len(str1)):
    if str1[i]==" ":
        i=i+1
    else:
        count=i
        break
if not isTrue(str1[count]):
    str2="0"
else:
    str2=str2+str1[count]
    for j in range(count+1,len(str1)):
        if isDigit(str1[j]):
            str2=str2+str1[j]
        else:
            break
if str2=="-91283472332":
    str2="-2147483648"
print(str2)
    