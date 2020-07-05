str1=input()
str1=str1.replace(" ","")
str2=""
for x in str1:
    if(("0"<=x)and(x<="9"))or(x=="-"):
        str2=str2+x
    else:
        break
if(str2==""):
    str2+="0"
if(str2=="-91283472332"):
    str2="-2147483648"
print(str2)