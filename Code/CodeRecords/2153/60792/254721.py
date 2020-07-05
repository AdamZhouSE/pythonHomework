num=int(input())
str1=str(num)
if num>=0:
    str2=str1[::-1]
    i=0
    while str2[i]=="0":
        i=i+1
    str2=str2[i:]
else:
    str3=str1[1:]
    str3=str3[::-1]
    i=0
    while str3[i]=="0":
        i=i+1
    str2="-"+str3[i:]
print(str2)