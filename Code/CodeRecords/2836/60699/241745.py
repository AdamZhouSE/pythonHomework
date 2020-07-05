input()
list1=list(map(int,input().split(' ')))
index=1
while index<len(list1):
    if list1[index]<list1[index-1]:
        break
    index+=1
temp=index
index+=1
flag=True
while index<len(list1):
    if list1[index]<list1[index-1]:
        flag=False
    index+=1
if list1[len(list1)-1]>list1[0]:
    flag=False
if flag:
    print(len(list1)-temp)
else:
    print(-1)