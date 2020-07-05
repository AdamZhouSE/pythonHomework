str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
num=[]
ans=-1
for i in range(len(list1)):
    num.append(int(list1[i]))
tar=int(input())
for i in range(len(num)):
    if num[i]==tar:
        ans=i
        break
print(ans)
