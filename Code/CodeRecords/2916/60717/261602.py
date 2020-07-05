n=int(input())
list0=[4,8,15,16,23,42]
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=[]
list2.append(list1.count(4))
list2.append(list1.count(8))
list2.append(list1.count(15))
list2.append(list1.count(16))
list2.append(list1.count(23))
list2.append(list1.count(42))
count=0
while not(0 in list2):
    flag=1
    for i in range(0,5):
        if list1.index(list0[i])>list1.index(list0[i+1]):
            list1.remove(list0[i+1])
            list2[i+1]-=1
            count+=1
            flag=0
            break
    if flag==1:
        for i in list0:
            list1.remove(i)
        for i in range(0,6):
            list2[i]-=1
print(count+len(list1))