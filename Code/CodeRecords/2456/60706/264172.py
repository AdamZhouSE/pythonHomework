str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
ans=[]
for i in range(len(list1)):
    count=0
    for j in range(i+1,len(list1)):
        if int(list1[i])>int(list1[j]):
            count=count+1
    ans.append(count)
print(ans)