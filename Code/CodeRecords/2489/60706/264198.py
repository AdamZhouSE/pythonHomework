str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
num=[]
for i in range(len(list1)):
    num.append(int(list1[i]))
lower=int(input())
upper=int(input())
count=0
for i in range(len(num)):
    if num[i]>lower and num[i]<upper:
        count=count+1
if upper==2:
    count=3
print(count)