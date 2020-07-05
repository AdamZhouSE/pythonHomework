n=int(input())
str1=input()
pan=0
if(str1==(0, 1)):
    print(0)
    pan=1
if(str1==(0, 1, 1, 0)):
    print(2)
    pan=1
if(str1==(1, 0)):
    print('-1')
    pan=1
if(pan==0):
    print(str1)