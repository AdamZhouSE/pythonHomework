str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
num1=0
for i in range(len(list1)):
    if list1[i]=='null':
        num1=num1+1
for i in range(num1):
    list1.remove('null')
str2=input()
str2=str2.replace('[','')
str2=str2.replace(']','')
list2=str2.split(',')
num2=0
for i in range(len(list2)):
    if list2[i]=='null':
        num2=num2+1
for i in range(num2):
    list2.remove('null')
ans=[]
for i in range(len(list1)):
    if list1[i]!='':
        ans.append(int(list1[i]))
for i in range(len(list2)):
    if list2[i]!='':
        ans.append(int(list2[i]))
for i in range(len(ans)):
    for j in range(i+1,len(ans)):
        if ans[i]>ans[j]:
            ans[i],ans[j]=ans[j],ans[i]
print(ans)
