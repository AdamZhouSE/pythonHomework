str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
num=[]
for i in range(len(list1)):
    num.append(int(list1[i]))
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print(num)