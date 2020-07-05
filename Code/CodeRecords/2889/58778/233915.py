n=int(input())
str=input()
list1=str.split( )
count=0
for i in list1:
    count=count+int(i)
print('%.6f'%(count/(n)))  