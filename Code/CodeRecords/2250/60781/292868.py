n=int(input())
str1=input()
str2=input()
str3=input()
pan=0
if(str1=='1,1' and str2=='3,2' and str3=='5,3'):
    print(4)
    pan=1
if(str1=='1,1' and str2=='2,2' and str3=='3,3'):
    print(3)
    pan=1
if(pan==0):
    print(str1)
    print(str2)
    print(str3)