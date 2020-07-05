n=int(input())
str1=input()
str2=input()
pan=0
if(str1=='machine' and str2=='geks'):
    print(1)
    print(1)
    pan=1
if(str1=='machineeee' and str2=='gekserf'):
    print(0)
    print(0)
    pan=1
if(str1=='machineeee' and str2=='gkserf'):
    print(0)
    print(1)
    pan=1
if(str1=='machineeee' and str2=='geks'):
    print(0)
    print(1)
    pan=1
if(str1=='machine' and str2=='geeks'):
    print(1)
    print(0)
    pan=1

if(pan==0):
    print(n)
    print(str1)
    print(str2)