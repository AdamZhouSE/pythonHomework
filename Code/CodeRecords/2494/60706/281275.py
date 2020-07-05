str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
num=[]
for i in range(len(list1)):
    num.append(int(list1[i]))
count=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>2*num[j]:
            count=count+1
print(count)