str=input()
str=str[1:len(str)-1]
str=str.split(",")
num=int(input())
sig=0
for i in range (0,len(str)):
    str[i]=int(str[i])
for i in range (1,len(str)):
   if(num==str[i]):
       sig=1
       print(i)
       break;
if(sig==0):
    print(-1)
    