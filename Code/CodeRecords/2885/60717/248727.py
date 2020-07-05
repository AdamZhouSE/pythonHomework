n=int(input())
for i in range(0,n):
    a=int(input())
    list1=input().split()
    for j in range(0,a):
        list1[j]=int(list1[j])
    list2=[]
    list3=[]
    count=0
    for j in range(0,a):
        if list1[j]%3==0:
            count+=1
        elif list1[j]%3==1:
            list2.append(list1[j])
        elif list1[j]%3==2:
            list3.append(list1[j])
    while len(list2)!=0 and len(list3)!=0:
        list2.pop()
        list3.pop()
        count+=1
    if len(list2)==0:
        print(count+int(len(list3)/3))
    else:
        print(count+int(len(list2)/3))
            