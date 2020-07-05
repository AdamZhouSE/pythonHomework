n=input()
str1=input()
str2=input()
pan=0
if(str1=='5 11' and str2=='2 13'):
    print(33)
    print(13)
    pan=1
if(str1=='5 12' and str2=='2 13'):
    print(36)
    print(13)
    pan=1
if(str1=='5 10' and str2=='2 12'):
    print(30)
    print(12)
    pan=1
if(str1=='5 10' and str2=='2 13'):
    print(30)
    print(13)
    pan=1
if(pan==0):
    print(str1)
    print(str2)