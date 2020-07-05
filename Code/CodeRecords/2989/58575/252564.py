str1=input()
str2=input()
str3=input()
if str1>str2:
    temp=str1
    str1=str2
    str2=temp
if str3<str1:
    print(str3,"\n",str1,"\n",str2,sep="")
elif str3<str2:
    print(str1,"\n",str3,"\n",str2,sep="")
else:
    print(str1,"\n",str2,"\n",str3,sep="")
    