num=int(input())
length=int(input())
Str=input()
list=Str.split(" ")
numlist1=[0]*length
numlist2=[0]*length

for i in range(0,len(numlist1)):
    numlist1[i]=int(list[i])
    numlist2[i]=int(list[i])
max1=0
max2=0
#整数相乘
a=max(numlist1)
numlist1.remove(a)
b=max(numlist1)
numlist1.remove(b)
c=max(numlist1)
numlist1.remove(c)
max1=a*b*c
a=min(numlist2)
numlist2.remove(a)
b=min(numlist2)
numlist2.remove(b)
c=max(numlist2)
numlist2.remove(c)
max2=a*b*c
if(max1>max2):
    print(max1)
else:
    print(max2)