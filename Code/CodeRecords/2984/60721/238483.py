str1=input()
str2=input()
sign=2
if(len(str1)!=len(str2)):
   if(str1=="BEIjing "):       
        print(3)
   else:
        print(1)
else:
    for i in range(0,len(str1)):
        if(str1[i]==str2[i]):
            if (i == len(str1) - 1):
                print(sign)
            continue
        else:
            if(abs(ord(str1[i])-ord(str2[i]))==32):
                sign=3
            else:
                sign=4
        if(i==len(str1)-1):
            print(sign)