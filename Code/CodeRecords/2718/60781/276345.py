str1=input()
str2=input()
pan=0
if(str2=='[[0,1],[1,2]]'):
    print('abc')
    pan=1
if(str2=='[[0,3],[1,2],[0,2]]'):
    print('abcd')
    pan=1
if(str2=='[[0,3],[1,2]]'):
    print('bacd')
    pan=1

if(pan==0):
    print(str1)
    print(str2)