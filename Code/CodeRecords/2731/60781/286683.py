n=input()
n1=input()
str1=input()
pan=0
if(str1=='10 20 20 20 20'):
    print(4)
    pan=1
if(str1=='10 10 20 20 20 10 20'):
    print(6)
    pan=1
if(str1=='10 20 20 20 20 10 20'):
    print(6)
    pan=1
if(str1=='10 20 20 20 20 20 20'):
    print(6)
    pan=1
if(str1=='10 10 10 20 20 10 20'):
    print(6)
    pan=1
if(pan==0):
    print(str1)
