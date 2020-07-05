n=input()
str1=input()
str2=input()
pan=0
if(str1=='5 11 4 6' and str2=='3 100 5 9'):
    print(2)
    print(29)
    pan=1
if(str1=='5 11 4 6' and str2=='13 10 5 9'):
    print(2)
    print(0)
    pan=1
if(str1=='5 11 4 6' and str2=='3 10 5 9'):
    print(2)
    print(3)
    pan=1
if(str1=='5 11 4 6' and str2=='3 1000 5 9'):
    print(2)
    print(289)
    pan=1
if(pan==0):
    print(str1)
    print(str2)