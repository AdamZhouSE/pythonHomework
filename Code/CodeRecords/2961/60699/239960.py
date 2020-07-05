str1=input()
list1=[]
list1.append(str1)
for i in range(1,len(str1)):
    list1.append(str1[i:]+str1[0:i])
list1.sort()
k=len(str1)
res=""
for i in list1:
    res+=i[k-1]
print(res,end='')