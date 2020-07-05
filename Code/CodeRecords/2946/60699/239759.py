str1 = input()
list1=[]
for i in str1:
    list1.append(i)
list1.reverse()
index=0
res=0
k=len(list1)
while index<k:
    if list1[index]=='1':
        index+=1
    else:
        res+=1
        list2=[]
        for j in range(0,k):
            if j<=index:
                list2.append('1')
            else:
                if list1[j]=='0':
                    list2.append('1')
                else:
                    list2.append('0')
                
        list1=list2
        index+=1
print(res,end='')